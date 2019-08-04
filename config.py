import json

from telethon.sync import TelegramClient
from telegram.ext import Updater


# Import config file
with open('config.json') as config_file:
    data = json.load(config_file)

# User Config (telethon)
user_client = TelegramClient(
    data['user']['session_name'],
    data['user']['api_id'],
    data['user']['api_hash']
)

# Bot config (python-telegram-bot)
bot_updater = Updater(
    data['bot']['token']
)
