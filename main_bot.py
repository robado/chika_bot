import discord
import os
from discord.ext import commands

from dotenv import load_dotenv
from pathlib import Path
env_path = Path('config/') / '.env'
load_dotenv(dotenv_path=env_path, verbose=True)

command_prefix = 'chika'
chika = commands.Bot(command_prefix=command_prefix)
API_KEY = os.getenv("API_KEY")

# Get random images/gifs locally on specific subject

# Get random images/gifs from internet on specific subject

# https://stackoverflow.com/questions/53218027/how-would-i-use-the-giphy-python-api-with-my-discord-bot
# https://github.com/MRmlik12/Tenor-Bot-Discord/blob/master/tenor.py
# https://github.com/theskumar/python-dotenv

# get all the cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        chika.load_extension(f'cogs.{filename[:-3]}')

chika.run(API_KEY)
