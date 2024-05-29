import dotenv
import time
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from models.command import *

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
        bot.send_message(message.chat.id, welcome)

        if check_user(message.chat.id):
            inline_btn = InlineKeyboardMarkup(row_width=2).add(inline_btn2, inline_btn3, inline_btn4, price)
            bot.send_message(message.chat.id, 'Мы уже с вами знакомы :) ', reply_markup=inline_btn)
        else:
            bot.send_message(message.from_user.id, 'Введите свое имя и фамилию')
            bot.register_next_step_handler(message, input_user)

    @bot.callback_query_handler(func=lambda call: call.data == 'check_records')
    def check_records(call):

        bot.send_message(call.message.chat.id, 'Посмотреть записи')

    @bot.callback_query_handler(func=lambda call: call.data == 'add_record')
    def add_record(call):
        inline_btn = InlineKeyboardMarkup().add(inline_btn5, inline_btn6, inline_btn7, inline_main)
        bot.send_message(call.message.chat.id, 'Выберите услугу: ', reply_markup=inline_btn)

    @bot.callback_query_handler(func=lambda call: call.data == 'delete_record')
    def del_records(call):
        bot.send_message(call.message.chat.id, 'Отменить запись')

    @bot.callback_query_handler(func=lambda call: call.data == 'Nails')
    def nails(call):
        inline_btn = InlineKeyboardMarkup().add(inline_btn8, inline_btn9, inline_main)
        bot.send_message(call.message.chat.id, 'nails', reply_markup=inline_btn)

    @bot.callback_query_handler(func=lambda call: call.data == 'Hair')
    def nails(call):
        bot.send_message(call.message.chat.id, 'Hair')

    @bot.callback_query_handler(func=lambda call: call.data == 'Eyelash')
    def nails(call):
        bot.send_message(call.message.chat.id, 'Eyelash')

    @bot.callback_query_handler(func=lambda call: call.data == 'main_menu')
    def main_menu(call):
        inline_btn = InlineKeyboardMarkup(row_width=2).add(inline_btn2, inline_btn3, inline_btn4, price)
        bot.send_message(call.message.chat.id, 'Выберите действие: ', reply_markup=inline_btn)

    @bot.callback_query_handler(func=lambda call: call.data == 'price')
    def get_price(call):
        bot.send_message(call.message.chat.id, price_message,
                         reply_markup=InlineKeyboardMarkup().add(inline_main))

    def input_user(message):
        fi = message.text
        add_user(message.chat.id, fi)
        bot.send_message(message.from_user.id, f'Приятно с вами познакомиться, {fi}!\nВведите номер телефона:')
        bot.register_next_step_handler(message, input_number)

    def input_number(message):
        number = message.text
        add_phone_number(message.chat.id, number)
        inline_btn = InlineKeyboardMarkup().add(inline_btn2, inline_btn3, inline_btn4, price)
        bot.send_message(message.chat.id, 'Регистрация прошла успешно! Теперь можете выбирать процедуры!',
                         reply_markup=inline_btn)

    bot.polling(non_stop=True)
    print('Bot stop')


if __name__ == '__main__':
    main()
