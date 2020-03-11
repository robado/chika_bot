print("==========")
print("Chika Bot")
print("==========")

import discord
import os
from discord.ext import commands

chika = commands.Bot(command_prefix='.')

# Events
"""@chika.event
async def on_ready():
    print("Bot is ready")
"""



@chika.event
async def on_member_join(member):
    print('{} has joined a server.'.format(member))


@chika.event
async def on_member_remove(member):
    print(f'{member} has left the server.')


# Commands
# bot says konnichiwa
@chika.command()
async def konnichiwa(ctx):
    await ctx.send("Konnichiwa")


# send text
@chika.command()
async def send(ctx, *, args):
    await ctx.send(args)


# clears text
@chika.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


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

chika.run('token here')
