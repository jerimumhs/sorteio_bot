import random
import json

from telegram.ext import CommandHandler
from telegram import ParseMode
from loguru import logger

from config import bot_updater, data
from helpers import restricted, get_users_group


@restricted
def get_random_participant(bot, update):
    '''
    Get a random participant from the user.json file.
    '''
    with open('users.json') as user_file:
        participants_list = json.load(user_file)

    participant = random.choice(participants_list)
    update.message.reply_text(
        f'[{participant["full_name"]}](tg://user?id={participant["id"]})',
        parse_mode=ParseMode.MARKDOWN
    )


def bot():
    '''
    Initialize the bot.
    '''
    get_users_group(data['group']['name'])

    bot_updater.dispatcher.add_handler(
        CommandHandler(
            'sorteio',
            get_random_participant
        )
    )

    bot_updater.start_polling()
    bot_updater.idle()


if __name__ == "__main__":
    bot()
