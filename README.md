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
Ideas of function for this bot

* Welcome message on user joining  
    * ~~Displays a welcoming message~~ 
    * ~~With message display a pic~~ 
    * ~~Or a gif~~
    * Add a helpful tip to footer f.ex what is the prefix
    * Send joined member a private message??? 
    * Randomize a welcoming message
* Embedded messages
    * ~~In welcome message~~
    * when command send message (when necessary)
* Make a help commands to show all the commands + explanations
    * Either modify old one
        * By adding *brief* & *description* to *command()*
    * Or make a brand new one help menu
* Add errors for necessary commands or actions
    * And error for every command/action would be great - but probably not necessary
* Chika can give a cola
    * ~~Displays a picture of Chika giving a cola~~ 
    * ~~Sender can specify user~~
    * ~~Mentions a user~~
    * ~~If no user was mentioned then mention sender~~
* Chika dance
    * Chika dance gif
        * Choose a random "Chika dance" gif from giphy or tenor
* ~~Chika can bong you~~
    * ~~Send a gif with chika bong~~
    * ~~Mention user and the bonging person~~
    * ~~If no user was tagged give an error~~
* Add daily a image related to Chika anime
    * ~~From reddit~~
    * Need to choose a source for this???
* Randomly spams a Chika gif or pic
    * When giving a commands bot will spam gif or a pic
    * Source???
* ~~Move code commands & events to cogs~~
    * ~~For code tidiness~~
* Store data (maybe)
    * For example users
    * How many messages was sent
* Role specific commands
    * For example admins have ban, kick. Mods could have rename
* Restrict on commands on channels
    * Restrict where specific commands can be used on which channels
        * ~~ban, unban, kick for admin only~~
* Send DM
* Add config file for config stuff
    * ~~Token~~
    * ~~Reddit config~~
    * If I want to store to database then database config
* Change users nickname??
    * Either a specific one or a random??
* Automatically assign role
    * This can be via join
    * Reacting to a post with emote
    * With commands
* Reddit
    * Make post daily posts from specific subreddit
        * ~~From /r/ChikaFujiwara/~~~
    * A user can assign a bot to post new posts from subreddit
        * This prob has to be restricted to how many user can make
* Steam???
* Twitter???
* Make a Trello board of this
    * This is getting pretty messy - Trello could make it easier to read

##### Stuff for later
* Make bot run in Docker container
* Deploy to [heroku](https://www.heroku.com/)
    * It has a free plan for hobbyist!
    * Make it to deploy newest version from [Github](https://github.com/)
    
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
> git clone https://github.com/robado/chika_bot.git

After code is downloaded install virtual environment for the project.
> cd chika_bot/
**linux:** python3 -m venv bot-env / **windows:** python -m venv bot-env

Then activate the virtual environment and install the necessary packages.
> **Linux:** source bot-env/bin/activate / **Windows:** .\bot-env\Scripts\activate
> **Linux:** pip install -r requirements.txt / **Windows:** pip install -r requirements.txt 

After the installation in complete the bot can be ran. Change these values with your own.
> Linux: python3 main.py / Windows: python main_bot.py

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
