Devico Notifications Bot
=====

This bot is designed to track the learning process at Devman. 
The bot checks the status of the job sent for verification and 
sends notifications with the status text.


Built With
-------------

* [Python Telegram Bot](https://python-telegram-bot.readthedocs.io/) - library provides a pure Python interface for the Telegram Bot API
* [Requests](http://docs.python-requests.org/) - Elegant and simple HTTP library for Python
* [Logging](https://docs.python.org/3/library/logging.html#/) - Logging facility for Python


Installing
----------

Install and update using `pip`_:

.. code-block:: text

    pip install -r requirements.txt
    

Basic usage
-----------

Create .env file with two tokens
* TELEGRAM_TOKEN
* DEVMAN_TOKEN

Run on development enviroment:

.. code-block:: text

    python bot.py


Deployment
----------

Use Heroku for deploy.

Install the Heroku CLI
Download and install the Heroku CLI.

If you haven't already, log in to your Heroku account and follow the prompts 
to create a new SSH public key.

.. code-block:: text

    $ heroku login
Clone the repository
Use Git to clone devico-notifications-bot's source code to your local machine.

.. code-block:: text

    $ heroku login
    $ heroku git:clone -a devico-notifications-bot
    $ cd devico-notifications-bot    
    
Deploy your changes
Make some changes to the code you just cloned and deploy them to Heroku using Git.

.. code-block:: text

    $ git add .
    $ git commit -am "make it better"
    $ git push heroku master


Links
-----

* Python Telegram Bot: https://python-telegram-bot.readthedocs.io/
* Requests: http://docs.python-requests.org/
* Logging: https://docs.python.org/3/library/logging.html#/
* Heroku: https://heroku.com
