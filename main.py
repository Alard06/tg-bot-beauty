import os
import dotenv
import time
import telebot
from telebot.types import InlineKeyboardMarkup

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
        bot.send_message(message.chat.id, welcome, reply_markup=inline_btn)

    @bot.callback_query_handler(func=lambda call: call.data == "start_button")
    def start_button(call):
        bot.answer_callback_query(call.id)
        bot.send_message(call.from_user.id, 'Кнопка нажата')

    bot.infinity_polling()
    print('Bot stop')




if __name__ == '__main__':
    main()
