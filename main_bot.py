import discord
import os
from discord.ext import commands

import logging

from dotenv import load_dotenv
from pathlib import Path
# path to .env
env_path = Path('config/') / '.env'
load_dotenv(dotenv_path=env_path, verbose=True)

command_prefix = 'chika'
chika = commands.Bot(command_prefix=command_prefix)
TOKEN = os.getenv("TOKEN")

logging.basicConfig(level=logging.INFO) # DEBUG

# get all the cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        chika.load_extension(f'cogs.{filename[:-3]}')

chika.run(TOKEN)
