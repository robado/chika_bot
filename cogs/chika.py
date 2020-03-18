import discord
from discord.ext import commands


class Chika(commands.Cog):

    def __init__(self, chika):
        self.chika = chika

    @commands.command(brief='Cola', description='Chika gives you Cola')
    async def cola(self, ctx,):
        embed = discord.Embed(title='', description='Here is your cola')
        file = discord.File('gifs/chikaCola.gif', filename='chikaCola.gif')

        embed.set_image(url='attachment://chikaCola.gif')
        embed.set_footer(text='This is not a bribe')

        await ctx.send(file=file, embed=embed)


def setup(chika):
    chika.add_cog(Chika(chika))
