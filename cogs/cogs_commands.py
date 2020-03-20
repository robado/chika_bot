import discord
from discord.ext import commands


class CogsCommands(commands.Cog):

    def __init__(self, chika):
        self.chika = chika

    @commands.command(hidden=True)
    @commands.has_permissions(administrator=True)
    async def load(self, ctx, extension):  # Loads extension
        try:
            self.chika.load_extension(f'cogs.{extension}')
        except Exception as e:
            return await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            await ctx.send(f'Loaded extension {extension}')

    @commands.command(hidden=True)  # Unloads extension
    @commands.has_permissions(administrator=True)
    async def unload(self, ctx, extension):
        try:
            self.chika.unload_extension(f'cogs.{extension}')
        except Exception as e:
            return await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            await ctx.send(f'Unloaded extension {extension}')

    @commands.command(hidden=True)  # unloads then reloads
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx, extension: str):
        try:
            self.chika.unload_extension(f'cogs.{extension}')
            self.chika.load_extension(f'cogs.{extension}')
        except Exception as e:
            return await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            await ctx.send(f'Reloaded extension {extension}')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title='', description=f'Dont forget to specify the cog!')
            await ctx.send(embed=embed)


def setup(chika):
    chika.add_cog(CogsCommands(chika))
