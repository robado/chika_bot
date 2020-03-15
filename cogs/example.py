import discord
from discord.ext import commands


class Example(commands.Cog):

    def __init__(self, chika):
        self.chika = chika

    # Commands
    @commands.command(brief='Ping', description='Pongs you back')
    async def ping(self, ctx):
        await ctx.send("Pong!")


def setup(chika):
    chika.add_cog(Example(chika))
