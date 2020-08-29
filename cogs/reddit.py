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
        # Empty list to check to check duplicates
        duplicate_check_list = []

        # praw config - prob can make in a different method
        # reddit = praw.Reddit() # Couldn't not make praw.ini work
        reddit = praw.Reddit(client_id=os.getenv("CLIENT_ID"),
                             client_secret=os.getenv("CLIENT_SECRET"),
                             password=os.getenv("PASSWORD"),
                             user_agent=os.getenv("USER_AGENT"),
                             username=os.environ.get("REDDIT_USERNAME"))

        channel = self.chika.get_channel(int(os.environ.get("DISCORD_CHANNEL_ID")))  # specific channel
        colour = discord.colour.Color.red()

        # while not self.chika.is_closed: I think this blocks the whole thing
        # Get the post
        for posts in reddit.subreddit(os.environ.get("SUBREDDIT")).stream.submissions(pause_after=0):
            if posts is None:
                # Wait 60 seconds for new submission
                await asyncio.sleep(60)
            elif posts.created_utc > current_date_in_seconds:
                print("New post was found. With id: {} and created time was: {}".format(posts.id, time.strftime(
                    '%Y-%m-%d %H:%M:%S', time.localtime(posts.created_utc))))
                if posts.id in duplicate_check_list: # First checking if id is in list, if yes then return.
                    print("Duplicate id: {}! Returning...".format(posts.id))
                    return
                else:
                    print("Id: {} was not duplicate. Clearing and updating list!".format(posts.id))
                    duplicate_check_list.clear()
                    duplicate_check_list.append(posts.id)
                    if posts.is_self == True and posts.is_reddit_media_domain == False and posts.is_video == False: # If text only
                        print("A new text post was posted with id: {}".format(posts.id))
                        await channel.send(embed=embed_maker(posts.title, posts.url, posts.selftext, colour, posts.subreddit_name_prefixed, posts.author, posts.over_18, posts.ups)) # This is much cleaner ....
                    if posts.is_self == False and posts.is_reddit_media_domain == True and posts.is_video == False:  # If image:
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
                    if posts.is_self == False and posts.is_reddit_media_domain == True and posts.is_video == True:  # If video
                        post_dict = vars(posts)
                        print("A new video post was posted with id: {}".format(posts.id))
                        embed = discord.Embed(title='{}'.format(posts.title),
                                            url='{}{}'.format(os.environ.get("REDDIT_BASE_URL"), posts.permalink),
                                            colour=colour)
                        embed.set_author(name='New video post on {}'.format(posts.subreddit_name_prefixed),
                                        url=posts.url)
                        embed.add_field(name='Author',
                                        value='{}'.format(posts.author),
                                        inline=True)
                        embed.add_field(name='NSFW',
                                        value='{}'.format(posts.over_18),
                                        inline=True)
                        embed.set_image(url='{}'.format(post_dict['preview']['images'][0]['source']['url'])) # I could getting the data like this in every place...
                        embed.set_footer(text='Ups: {}'.format(posts.ups))
                        await channel.send(embed=embed)
            # await asyncio.sleep(60) # This didnt work and still sends multiple of the same post

def setup(chika):
    chika.add_cog(RedditPosts(chika))

# This could make with optional arguments so any embed for reddit would be valid here
def embed_maker(post_title, post_url, post_selftext, embed_colour, subreddit_name_prefixed, posts_author, post_over_18, post_ups):
    embed = discord.Embed(title='{}'.format(post_title),
                        url=post_url,
                        description='{}'.format((post_selftext[:2045] + '...') if len(
                            post_selftext) > 2048 else post_selftext),
                        colour=embed_colour)
    embed.set_author(name='New text post on {}'.format(subreddit_name_prefixed),
                    url='{}'.format(post_url))
    embed.add_field(name='Author',
                    value='{}'.format(posts_author),
                    inline=True)
    embed.add_field(name='NSFW',
                    value='{}'.format(post_over_18),
                    inline=True)
    embed.set_footer(text='Ups: {}'.format(post_ups))
    return embed