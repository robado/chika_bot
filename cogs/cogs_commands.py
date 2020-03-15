import discord
from discord.ext import commands

"""
Error checking must be add
"""


class CogsCommands(commands.Cog):

    def __init__(self, chika):
        self.chika = chika

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def load(self, ctx, extension):  # Loads extension
        try:
            self.chika.load_extension(f'cogs.{extension}')
        except Exception as e:
            return await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            await ctx.send(f'Loaded extension {extension}')

    @commands.command(administrator=True)  # Unloads extension
    async def unload(self, ctx, extension):
        try:
            self.chika.unload_extension(f'cogs.{extension}')
        except Exception as e:
            return await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            await ctx.send(f'Unloaded extension {extension}')

    @commands.command(administrator=True)  # unloads then reloads
    async def reload(self, ctx, extension):
        try:
            self.chika.unload_extension(f'cogs.{extension}')
            self.chika.load_extension(f'cogs.{extension}')
        except Exception as e:
            return await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            await ctx.send(f'Loaded extension {extension}')


def setup(chika):
    chika.add_cog(CogsCommands(chika))
