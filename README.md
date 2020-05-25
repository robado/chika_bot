# Discord Chika Fujiwara Bot
Attempt to make some kind of an awesome Discord bot using [discord.py](https://discordpy.readthedocs.io/en/latest/).

## Table of context 
- [To-do List](#to-do-list)
- [How to run locally](#how-to-run-locally)
    - [Installing Python](#installing-python)
    - [Pip](#pip)
    - [Pipenv](#pipenv)
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
* Chika can bong you
    * ~~Send a gif with chika bong~~
    * ~~Mention user and the bonging person~~
    * ~~If no user was tagged give an error~~
* Add daily a image related to Chika anime
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
    * ~~For example token~~
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
Running locally you need to Python 3.7, pip 20.0.2 and pipenv==2018.11.26. (These are the versions I used to make
 this bot, but probably with earlier version it would work).

### `Installing Python`  
Python you can download from [Python website](https://www.python.org/downloads/).

### `Pip`  
Pip should come when you install Python. But if not for some reason you can install it via this [link](https://pip.pypa.io/en/stable/installing/)

### `pipenv`  
Pipenv can be installed via this [link](https://pipenv-fork.readthedocs.io/en/latest/install.html#pragmatic-installation-of-pipenv)

### `Running bot locally`  
Finally when you have everything installed you can build this project and run locally. 
* This will be updated! Currently no instructions on how to run locally!!!

Firstly create a token.txt where you will store your bots token. This file is excluded from GitHub repository because
 bots have uniques tokens.  
## Useful links
* [Discord.py documentation](https://discordpy.readthedocs.io/en/latest/)
* [Helpful youtube tutorial by Lucas](https://www.youtube.com/watch?v=nW8c7vT6Hl4&list=PLW3GfRiBCHOhfVoiDZpSz8SM_HybXRPzZ)
* [Another useful tutorial by techwithtim](https://techwithtim.net/tutorials/discord-py/)
---
