import discord
from discord.ext import commands


class Chika(commands.Cog):

    def __init__(self, chika):
        self.chika = chika

    @commands.command(brief='Cola', description='Chika gives you or your friend a cola')  # Gives either yourself a
    # cola or to another user
    async def cola(self, ctx, member: discord.Member = None):
        if member:
            embed = discord.Embed(title='', description=f'Here is your cola {member.mention}')
        else:
            embed = discord.Embed(title='', description=f'Here is your cola {ctx.message.author.mention}')

        file = discord.File('gifs/chikaCola.gif', filename='chikaCola.gif')

        embed.set_image(url='attachment://chikaCola.gif')
        embed.set_footer(text='This is not a bribe')

        await ctx.send(file=file, embed=embed)

    @commands.command(brief='Bong', description='Chika bongs someone')  # Bongs user
    async def bong(self, ctx, member: discord.Member = None):
        if not member:
            embed = discord.Embed(title='',
                                  description=f'You need to @ a user!')
            file = discord.File('gifs/chikaAngry.gif', filename='chikaAngry.gif')

            embed.set_image(url='attachment://chikaAngry.gif')

            await ctx.send(file=file, embed=embed)
        else:
            embed = discord.Embed(title='',
                                  description=f'{ctx.message.author.mention} bongs {member.mention} with a paper broom')
            file = discord.File('gifs/chikaBong.gif', filename='chikaBong.gif')

            embed.set_image(url='attachment://chikaBong.gif')

            await ctx.send(file=file, embed=embed)


def setup(chika):
    chika.add_cog(Chika(chika))
