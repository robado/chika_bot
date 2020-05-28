import os
import discord
from discord.ext import commands

class RedditPosts(commands.Cog):
    def __init__(self, chika):
        self.chika = chika

    @commands.Cog.listener()
    async def reddit_new_post_fetch(self):
        print("Starting reddit")


def setup(chika):
    chika.add_cog(RedditPosts(chika))
