import discord
from discord.ext import commands


class Example(commands.Cog):

    def __init__(self, chika):
        self.chika = chika

    # Event
    @commands.Cog.listener()
    async def on_ready(self):
        # await self.chika.change_presence(status=discord.Status.idle, activity=discord.Game('Hello Chika'))
        print("Bot is ready")

    # Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")


def setup(chika):
    chika.add_cog(Example(chika))