import discord
from discord.ext import commands


class Admin(commands.Cog):

    def __init__(self, chika):
        self.chika = chika

    # clears text
    @commands.command()
    @commands.has_permissions(manage_messages=True)  # check if you have permissions to use this command
    # async def clear(ctx, amount=5):
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)

    # kick
    @commands.command(hidden=True)
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send('Kicked user {}'.format(member.mention))

    # ban
    @commands.command(hidden=True)
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send('Banned user {}'.format(member.mention))

    # unban
    @commands.command(hidden=True)
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()

        for ban_entry in banned_users:
            user = ban_entry.user
            await ctx.guild.unban(user)
            await ctx.send('Unbanned user {}.'.format(member))


def setup(chika):
    chika.add_cog(Admin(chika))
