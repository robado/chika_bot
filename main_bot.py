import discord
import os
from discord.ext import commands

command_prefix = 'chika'
chika = commands.Bot(command_prefix=command_prefix)


# Reads the token from file
def read_token():
    with open("token.txt") as token:
        line = token.readlines()
        return line[0].strip()


TOKEN = read_token()

# Get random images/gifs locally on specific subject

# Get random images/gifs from internet on specific subject

# https://stackoverflow.com/questions/53218027/how-would-i-use-the-giphy-python-api-with-my-discord-bot
# https://github.com/MRmlik12/Tenor-Bot-Discord/blob/master/tenor.py

# get all the cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        chika.load_extension(f'cogs.{filename[:-3]}')

chika.run(TOKEN)
