import discord
import os
from discord.ext import commands, tasks
from itertools import cycle

print("==========")
print("Chika Bot")
print("==========")

chika = commands.Bot(command_prefix='chika')
status = cycle(['Status 1', 'Status 2'])


# Reads the token from file
def read_token():
    with open("token.txt") as token:
        line = token.readlines()
        return line[0].strip()


TOKEN = read_token()
print(TOKEN)


# Events
@chika.event
async def on_ready():
    change_status.start()
    await chika.change_presence(status=discord.Status.idle, activity=discord.Game('Hello Chika'))
    print("Bot is ready")


# @chika.event
# async def on_message(message):
#     id = chika.get_guild(646815478244704267)
#
#     if message.content.find("!hello") != -1:
#         await message.channel.send("Hi")
#     elif message.content == "!users":
#         await message.channel.send(f"""# of Members: {id.member_count}""")  # We can use id.member_count


# Sends a msg on user join
@chika.event
async def on_member_join(member):
    channel = chika.get_channel(687060036303978501)
    await channel.send(f'Welcome to the Chika server {member.mention}')
    # await channel.send('http://i.imgur.com/TrNnPde.jpg%27')
    # for channel in member.guild.channels:
    # if str(channel) == 'konnichiwa':
    # await channel.send(f'Welcome to the Chika server {member.mention}')
    # print('{} has joined a server.'.format(member))


@chika.event
async def on_member_remove(member):
    print(f'{member} has left the server.')


# @chika.event
# async def on_command_error(ctx, error):
#    if isinstance(error, commands.CommandNotFound):
#        await ctx.send('Invalid command')
# if isinstance(error, commands.MissingRequiredArgument):
# await ctx.send('Please pass all required arguments')


# Commands
# bot says konnichiwa
@chika.command()
async def konnichiwa(ctx):
    await ctx.send(f'Konnichiwa {ctx.author}')


# send text
@chika.command()
async def send(ctx, *, args):
    await ctx.send(args)


# clears text
@chika.command()
@commands.has_permissions(manage_messages=True)  # check if you have permissions to use this command
# async def clear(ctx, amount=5):
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)


# @clear.error
# async def clear_error(ctx, error):
#     if isinstance(error, commands.MissingRequiredArgument):
#         await ctx.send('Please specify amount of messages to delete')


# kick and ban
@chika.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send('Kicked user {}'.format(member.mention))


@chika.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send('Banned user {}'.format(member.mention))


# unban
@chika.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()

    for ban_entry in banned_users:
        user = ban_entry.user
        await ctx.guild.unban(user)
        await ctx.send('Unbanned user {}.'.format(member))


# cogs
@chika.command()
async def load(ctx, extension):
    chika.load_extension(f'cogs.{extension}')


@chika.command()
async def unload(ctx, extension):
    chika.unload_extension(f'cogs.{extension}')


@chika.command()
async def reload(ctx, extension):
    chika.unload_extension(f'cogs.{extension}')
    chika.load_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        chika.load_extension(f'cogs.{filename[:-3]}')


# tasks
@tasks.loop(seconds=10)
async def change_status():
    await chika.change_presence(activity=discord.Game(next(status)))


# checks user id
def is_it_me(ctx):
    return ctx.author.id == 687727835712192534  # specific user id


# checks if command matches user id
@chika.command()
@commands.check(is_it_me)
async def example(ctx):
    await ctx.send(f'Hi i am {ctx.author}')


chika.run(TOKEN)
