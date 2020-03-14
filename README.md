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
    * Displays a welcoming message and a pic or a gif
* Embedded messages
* Add errors for necessary commands or actions
    * And error for every command/action would be great - but probably not necessary
* Chika can give a cola
    * Displays a picture of Chika giving a cola and mentions a user
* Randomly spams a Chika gif or pic
    * When giving a commands bot will spam gif or a pic
* Role specific commands
    * For example admins have ban, kick. Mods could have rename
* Change users nickname
    * Either a specific one or a random

##### Stuff for later
* Make bot run in Docker container
* Deploy to [heroku](https://www.heroku.com/)
    * It has a free plane for hobbyist!
    
## How to run locally
Running locally you need to Python 3.7, pip 20.0.2 and pipenv==2018.11.26. (These are the versions I used to make
 this bot, but probably with earlier version it would work).

`Installing Python`  
Python you can download from [Python website](https://www.python.org/downloads/).

`Pip`  
Pip should come when you install Python. But if not for some reason you can install it via this [link](https://pip.pypa.io/en/stable/installing/)

`pipenv`  
Pipenv can be installed via this [link](https://pipenv-fork.readthedocs.io/en/latest/install.html#pragmatic-installation-of-pipenv)

###`Running bot locally`  
Finally when you have everything installed you can build this project and run locally. 


Firstly create a token.txt where you will store your bots token. This file is excluded from GitHub repository because
 bots have uniques tokens.  
## Useful links
* [Discord.py documentation](https://discordpy.readthedocs.io/en/latest/)
* [Helpful youtube tutorial by Lucas](https://www.youtube.com/watch?v=nW8c7vT6Hl4&list=PLW3GfRiBCHOhfVoiDZpSz8SM_HybXRPzZ)
* [Another useful tutorial by techwithtim](https://techwithtim.net/tutorials/discord-py/)
---