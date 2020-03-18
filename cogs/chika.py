import discord
from discord.ext import commands


class Chika(commands.Cog):

    def __init__(self, chika):
        self.chika = chika

    @commands.command(brief='Cola', description='Chika gives you or your friend a cola')
    async def cola(self, ctx, member: discord.Member = None):
        if member:
            embed = discord.Embed(title='', description=f'Here is your cola {member.mention}')
        else:
            embed = discord.Embed(title='', description=f'Here is your cola {ctx.message.author.mention}')

        file = discord.File('gifs/chikaCola.gif', filename='chikaCola.gif')

        embed.set_image(url='attachment://chikaCola.gif')
        embed.set_footer(text='This is not a bribe')

        await ctx.send(file=file, embed=embed)


def setup(chika):
    chika.add_cog(Chika(chika))
