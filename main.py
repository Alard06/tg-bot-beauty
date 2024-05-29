import os
import dotenv
import time
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from

from messages.messages_client import *
from btn.main_btn import *


def main():
    dotenv.load_dotenv()
    config = dotenv.dotenv_values(".env")
    token = config["TOKEN"]
    bot = telebot.TeleBot(token)
    print('Bot started: ', time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()))

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        inline_btn = InlineKeyboardMarkup().add(inline_btn1)
        bot.send_message(message.chat.id, welcome)

        if check_user()

        bot.send_message(message.from_user.id, 'Введите свое имя и фамилию')
        bot.register_next_step_handler(message, input_user)

    def input_user(message):
        fi = message.text
        print()



    bot.infinity_polling()
    print('Bot stop')


if __name__ == '__main__':
    main()
