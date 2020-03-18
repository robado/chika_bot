import discord
from discord.ext import commands


class FunCommands(commands.Cog):

    def __init__(self, chika):
        self.chika = chika

    # ping chika.py and chika.py pong back
    @commands.command(brief='Ping', description='Pongs you back')
    async def ping(self, ctx):
        await ctx.send("Pong!")

    # bot says konnichiwa and mentions the user
    @commands.command(brief='brief', description='decription')
    async def konnichiwa(self, ctx):
        await ctx.send(f'Konnichiwa {ctx.message.author.mention}')

    # prints provided text
    @commands.command()
    async def send(self, ctx, *, args):
        await ctx.send(args)


def setup(chika):
    chika.add_cog(FunCommands(chika))
