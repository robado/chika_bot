import discord
from discord.ext import commands


class Events(commands.Cog):

    def __init__(self, chika):
        self.chika = chika

    # Event
    @commands.Cog.listener()
    async def on_ready(self):
        await self.chika.change_presence(status=discord.Status.idle, activity=discord.Game('Hello I\'m Chika'))
        print("==========")
        print("Chika Bot")
        print("==========")
        print("Bots cogs are ready")

    # Sends welcome message and tags user
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.chika.get_channel(687060036303978501)
        colour = discord.colour.Color.red()
        file = discord.File("gifs/chikaWelcome.gif", filename="chikaWelcome.gif")

        embed = discord.Embed(title='Chika Fujiwara',
                              description=
                              '''
                              Welcome to the best Chika server! 

                              Lets make this best server ever existing!

                              ''',
                              colour=colour)

        embed.set_image(url='attachment://chikaWelcome.gif')
        embed.set_footer(text='For help type chikahelp')

        embed.add_field(name='Remember!',
                        value='Weebs are allowed but also everyone else!')  # with {member.mention} user can be mentioned

        await channel.send(f'Welcome to the Chika server {member.mention}', file=file, embed=embed)

    # Does stuff on member leave
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left the server.')


def setup(chika):
    chika.add_cog(Events(chika))
