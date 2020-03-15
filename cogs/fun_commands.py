import discord
from discord.ext import commands


class FunCommands(commands.Cog):

    def __init__(self, chika):
        self.chika = chika

    # bot says konnichiwa and mentions the user
    @commands.command(brief='brief', description='decription')
    async def konnichiwa(self, ctx):
        await ctx.send(f'Konnichiwa {ctx.message.author.mention}')

    # prints provided text
    @commands.command()
    async def send(self, ctx, *, args):
        await ctx.send(args)

    # checks user id
    def is_it_me(self, ctx):
        return ctx.author.id == 239135830327689217  # specific user id

    # checks if command matches user id
    @commands.command()
    @commands.check(is_it_me)
    async def thisisme(self, ctx):
        await ctx.send(f'Hi i am {ctx.author}')


def setup(chika):
    chika.add_cog(FunCommands(chika))
