import os
import discord
from discord.ext import commands

import praw
import asyncio
from dotenv import load_dotenv
from pathlib import Path

# path to .env
env_path = Path('config/') / '.env'
load_dotenv(dotenv_path=env_path, verbose=True)


class RedditPosts(commands.Cog):
    def __init__(self, chika):
        self.chika = chika

    @commands.Cog.listener()
    async def on_ready(self):
        print("background on_ready")
        # background : https://github.com/Rapptz/discord.py/blob/master/examples/background_task.py
        # https://stackoverflow.com/questions/52334477/interact-with-background-task-with-commands-in-submodule-discord-py
        self.bg_task = self.chika.loop.create_task(self.reddit_new_post_fetch())

    @commands.command()
    # async def postNewRedditPost(self, ctx):
    async def reddit_new_post_fetch(self):
        print("Starting reddit")
        # praw config - prob can make in a different method
        reddit = praw.Reddit(client_id=os.getenv("CLIENT_ID"),
                             client_secret=os.getenv("CLIENT_SECRET"),
                             password=os.getenv("PASSWORD"),
                             user_agent=os.getenv("USER_AGENT"),
                             username=os.environ.get("REDDIT_USERNAME"))
        channel = self.chika.get_channel(688790390676914334)  # specific channel
        colour = discord.colour.Color.red()
        # Get the post
        # reddit_id_list =['gmxo79', 'gmyz32']
        # new_reddit=reddit.subreddit('robado_test_1').new(limit=1)
        for posts in reddit.subreddit(os.environ.get("SUBREDDIT")).stream.submissions():
            print('Post: ' + str(posts.id))
            # get posts with stream
            # check if post already posted (from list)
            # if not - post and add id to list
            # if dublicate - dont post
            # if nsfw - just add url

            if posts.is_self == True and posts.is_reddit_media_domain == False:
                print("This post does NOT contain image")
                # await channel.send('This post does not contain image: {}'.format(posts.id))
                # embed = discord.Embed(title='New post on subreddit /r/{}'.format({os.environ.get("SUBREDDIT")}),
                embed = discord.Embed(title='New text post on {}'.format(posts.subreddit_name_prefixed),
                                      url=posts.url,
                                      description='{}'.format(posts.selftext),
                                      colour=colour)
                embed.add_field(name='Author',
                                value='{}'.format(posts.author),
                                inline=True)
                embed.add_field(name='NSFW',
                                value='{}'.format(posts.over_18),
                                inline=True)
                await channel.send(embed=embed)
            if posts.is_self == False and posts.is_reddit_media_domain == True:
                print("This post DOES contain an image")
                await channel.send('This post DOES contain an image: {}'.format(posts.id))
            # make check for NSFW post
            await channel.send('await')
            await asyncio.sleep(30)


def setup(chika):
    chika.add_cog(RedditPosts(chika))

# check if post is only text (is_self:True (& is_reddit_media_domain:False)) -> post text with message
# if post is image/video (is_self:False & is_reddit_media_domain:True) -> post img in message
