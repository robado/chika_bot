import os
import discord
from discord.ext import commands

import praw
import asyncio
from dotenv import load_dotenv
from pathlib import Path
import time

# path to .env
env_path = Path('config/') / '.env'
load_dotenv(dotenv_path=env_path, verbose=True)
# current time
current_date_in_seconds = time.time()


class RedditPosts(commands.Cog):
    def __init__(self, chika):
        self.chika = chika

    @commands.Cog.listener()
    async def on_ready(self):
        # background : https://github.com/Rapptz/discord.py/blob/master/examples/background_task.py
        # https://stackoverflow.com/questions/52334477/interact-with-background-task-with-commands-in-submodule-discord-py
        self.bg_task = self.chika.loop.create_task(self.reddit_new_post_fetch())

    @commands.Cog.listener()
    async def reddit_new_post_fetch(self):
        await self.chika.wait_until_ready()
        print("Starting reddit")
        # praw config - prob can make in a different method
        # reddit = praw.Reddit() # Couldn't not make praw.ini work
        reddit = praw.Reddit(client_id=os.getenv("CLIENT_ID"),
                             client_secret=os.getenv("CLIENT_SECRET"),
                             password=os.getenv("PASSWORD"),
                             user_agent=os.getenv("USER_AGENT"),
                             username=os.environ.get("REDDIT_USERNAME"))
        channel = self.chika.get_channel(int(os.environ.get("DISCORD_BOT_SPAM_CHANNEL_ID")))  # specific channel
        colour = discord.colour.Color.red()
        # Get the post
        for posts in reddit.subreddit(os.environ.get("SUBREDDIT")).stream.submissions(pause_after=0):
            if posts is None:
                await asyncio.sleep(60)
            elif posts.created_utc > current_date_in_seconds:
                if posts.is_self == True and posts.is_reddit_media_domain == False:
                    # if posts.over_18 == True:
                    #     print("Content is over_18")
                    embed = discord.Embed(title='New text post on {}'.format(posts.subreddit_name_prefixed),
                                          url=posts.url,
                                          # description='{}'.format(posts.selftext),
                                          description='{}'.format((posts.selftext[:2045] + '...') if len(
                                              posts.selftext) > 2048 else posts.selftext),
                                          colour=colour)
                    embed.set_author(name='{}'.format(posts.title),
                                     url='{}'.format(posts.url))
                    embed.add_field(name='Author',
                                    value='{}'.format(posts.author),
                                    inline=True)
                    embed.add_field(name='NSFW',
                                    value='{}'.format(posts.over_18),
                                    inline=True)
                    embed.set_footer(text='Ups: {}'.format(posts.ups))
                    await channel.send(embed=embed)
                    if posts.is_self == False and posts.is_reddit_media_domain == True:
                        if posts.over_18 == True:
                            embed = discord.Embed(title='New image post on {}'.format(posts.subreddit_name_prefixed),
                                                  url=posts.url,
                                                  colour=colour)
                            embed.set_author(name='{}'.format(posts.title),
                                             url='{}{}'.format(os.environ.get("REDDIT_BASE_URL"), posts.permalink))
                            embed.add_field(name='Author',
                                            value='{}'.format(posts.author),
                                            inline=True)
                            embed.add_field(name='NSFW',
                                            value='{}'.format(posts.over_18),
                                            inline=True)
                            embed.set_footer(text='Ups: {}'.format(posts.ups))
                            await channel.send(embed=embed)
                        else:
                            embed = discord.Embed(title='New image post on {}'.format(posts.subreddit_name_prefixed),
                                                  url=posts.url,
                                                  colour=colour)
                            embed.set_author(name='{}'.format(posts.title),
                                             url='{}{}'.format(os.environ.get("REDDIT_BASE_URL"), posts.permalink))
                            #  embed.set_thumbnail(url='') <- if i want to use "compact mode" use thumbnail instead of
                            #  large pick
                            embed.add_field(name='Author',
                                            value='{}'.format(posts.author),
                                            inline=True)
                            embed.add_field(name='NSFW',
                                            value='{}'.format(posts.over_18),
                                            inline=True)
                            embed.set_image(url='{}'.format(posts.url))
                            embed.set_footer(text='Ups: {}'.format(posts.ups))
                            await channel.send(embed=embed)


def setup(chika):
    chika.add_cog(RedditPosts(chika))
