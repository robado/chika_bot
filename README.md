# Discord Chika Fujiwara Bot
Attempt to make some kind of an awesome Discord bot using [discord.py](https://discordpy.readthedocs.io/en/latest/).

## Table of context 
- [To-do List](#to-do-list)
- [How to run locally](#how-to-run-locally)
    - [Installing Python](#installing-python)
    - [Pip](#pip)
    - [Virtualenv](#virtualenv)
    - [Running locally](#running-bot-locally)
- [Useful links](#useful-links)

## To-Do List
Collecting ideas and possible functions for this bot in [Trello](https://trello.com/b/grMHlFWZ/chika-bot)

## How to run locally
Running locally you need to install Python 3, pip, pipenv and the necessary modules from requirements.txt. (These are
 the
 versions I used to
 make
 this bot, but probably with earlier version it would work).

### `Installing Python`  
Python you can download from [Python website](https://www.python.org/downloads/).

### `Pip`  
Pip should come when you install Python. But if not for some reason you can install it via this [link](https://pip.pypa.io/en/stable/installing/)

### `virtualenv`  
Pipenv can be installed via this [link](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

### `Running bot locally`  
Finally when you have everything installed you can build this project and run locally. 

First download the code.
```
git clone https://github.com/robado/chika_bot.git
```

After code is downloaded install virtual environment for the project.
```
cd chika_bot/
linux: python3 -m venv bot-env / windows: python -m venv bot-env
```

Then activate the virtual environment and install the necessary packages.
```
Linux: source bot-env/bin/activate / Windows: .\bot-env\Scripts\activate
Linux: pip install -r requirements.txt / Windows: pip install -r requirements.txt 
```

After the installation in complete the bot can be ran. Change these values with your own.
```
Linux: python3 main.py / Windows: python main_bot.py
```
In the file config/.env is stored the Discord bot's token. 
```
TOKEN=<TOKEN>

#Discord channel ids
DISCORD_CHANNEL_ID=<channel id> # This is for the bot-spam channel id

# reddit config
CLIENT_ID=<CLIENT_ID>
CLIENT_SECRET=<CLIENT_SECRET>
PASSWORD=<PASSWORD>
USER_AGENT=<USER_AGENT>
REDDIT_USERNAME=<REDDIT_USERNAME>

SUBREDDIT=<SUBREDDIT>
REDDIT_BASE_URL=<REDDIT_BASE_URL>
```

## Useful links
* [Discord.py documentation](https://discordpy.readthedocs.io/en/latest/)
* [Helpful youtube tutorial by Lucas](https://www.youtube.com/watch?v=nW8c7vT6Hl4&list=PLW3GfRiBCHOhfVoiDZpSz8SM_HybXRPzZ)
* [Another useful tutorial by techwithtim](https://techwithtim.net/tutorials/discord-py/)
---
