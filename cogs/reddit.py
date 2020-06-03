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
        # current time
        current_date_in_seconds = time.time()
        print("Starting reddit at {}".format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(current_date_in_seconds))))

        # praw config - prob can make in a different method
        # reddit = praw.Reddit() # Couldn't not make praw.ini work
        reddit = praw.Reddit(client_id=os.getenv("CLIENT_ID"),
                             client_secret=os.getenv("CLIENT_SECRET"),
                             password=os.getenv("PASSWORD"),
                             user_agent=os.getenv("USER_AGENT"),
                             username=os.environ.get("REDDIT_USERNAME"))

        channel = self.chika.get_channel(int(os.environ.get("DISCORD_CHANNEL_ID")))  # specific channel
        colour = discord.colour.Color.red()

        # Get the post
        for posts in reddit.subreddit(os.environ.get("SUBREDDIT")).stream.submissions(pause_after=0):
            if posts is None:
                await asyncio.sleep(60)
            elif posts.created_utc > current_date_in_seconds:
                print("New post was found. With id: {} and created time was: {}".format(posts.id, time.strftime(
                    '%Y-%m-%d %H:%M:%S', time.localtime(posts.created_utc))))
                if posts.is_self == True and posts.is_reddit_media_domain == False:
                    print("A new text post was posted with id: {}".format(posts.id))
                    # if posts.over_18 == True:
                    #     print("Content is over_18")
                    embed = discord.Embed(title='{}'.format(posts.title),
                                          url=posts.url,
                                          # description='{}'.format(posts.selftext),
                                          description='{}'.format((posts.selftext[:2045] + '...') if len(
                                              posts.selftext) > 2048 else posts.selftext),
                                          colour=colour)
                    embed.set_author(name='New text post on {}'.format(posts.subreddit_name_prefixed),
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
                        print("A new K-18 image post was posted with id: {}".format(posts.id))
                        embed = discord.Embed(title='{}'.format(posts.title),
                                              url='{}{}'.format(os.environ.get("REDDIT_BASE_URL"), posts.permalink),
                                              colour=colour)
                        embed.set_author(name='New image post on {}'.format(posts.subreddit_name_prefixed),
                                         url=posts.url)
                        embed.add_field(name='Author',
                                        value='{}'.format(posts.author),
                                        inline=True)
                        embed.add_field(name='NSFW',
                                        value='{}'.format(posts.over_18),
                                        inline=True)
                        embed.set_footer(text='Ups: {}'.format(posts.ups))
                        await channel.send(embed=embed)
                    else:
                        print("A new image post was posted with id: {}".format(posts.id))
                        embed = discord.Embed(title='{}'.format(posts.title),
                                              url='{}{}'.format(os.environ.get("REDDIT_BASE_URL"), posts.permalink),
                                              colour=colour)
                        embed.set_author(name='New image post on {}'.format(posts.subreddit_name_prefixed),
                                         url=posts.url)
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
            await asyncio.sleep(60)  # I think this is needed so the bot wont post duplicate... Because what I think
            # is happening that the program runs too fast and it picks up "new" aka the duplicate post a couple of
            # times.


def setup(chika):
    chika.add_cog(RedditPosts(chika))
