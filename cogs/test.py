import discord
from discord.ext import commands


class Test(commands.Cog):

    def __init__(self, chika):
        self.chika = chika

    @commands.command()
    async def test(self, ctx):
        await ctx.send('test')


def setup(chika):
    chika.add_cog(Test(chika))
