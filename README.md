Devico Notifications Bot
=====

This bot is designed to track the learning process at [Devman](https://dvmn.org/) 
The bot checks the status of the job sent for verification and 
sends notifications with the status text.


Built With
-------------

* [Python Telegram Bot](https://python-telegram-bot.readthedocs.io/) - library provides a pure Python interface for the Telegram Bot API
* [Requests](http://docs.python-requests.org/) - Elegant and simple HTTP library for Python
* [Logging](https://docs.python.org/3/library/logging.html#/) - Logging facility for Python


Installing
----------

Install and update using `pip`:

    pip install -r requirements.txt
    

Basic usage
-----------

Create .env file with two tokens
* TELEGRAM_TOKEN - token your bot for notifications
* DEVMAN_TOKEN - you api token of devman account
* USER_CHAT_ID - chat_id your telegram account (to get use @userinfobot in telegram)

Run on development enviroment:

    python bot.py


Deployment
----------

Use Heroku for deploy.

Install the Heroku CLI
Download and install the Heroku CLI.

If you haven't already, log in to your Heroku account and follow the prompts 
to create a new SSH public key.

    $ heroku login
Clone the repository
Use Git to clone devico-notifications-bot's source code to your local machine.

    $ heroku login
    $ heroku git:clone -a devico-notifications-bot
    $ cd devico-notifications-bot    
    
Deploy your changes
Make some changes to the code you just cloned and deploy them to Heroku using Git.

    $ git add .
    $ git commit -am "make it better"
    $ git push heroku master


Links
-----

* Python Telegram Bot: https://python-telegram-bot.readthedocs.io/
* Requests: http://docs.python-requests.org/
* Logging: https://docs.python.org/3/library/logging.html#/
* Heroku: https://heroku.com
