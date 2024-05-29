from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Смотреть записи / добавить запись
inline_btn2 = InlineKeyboardButton('Посмотреть записи', callback_data='check_records')
inline_btn3 = InlineKeyboardButton('Записаться мастеру', callback_data='add_record')
inline_btn4 = InlineKeyboardButton('Отменить запись', callback_data='delete_record')
inline_main = InlineKeyboardButton('Меню', callback_data='main_menu')
price = InlineKeyboardButton('Прайс', callback_data='price')

# Услуги

inline_btn5 = InlineKeyboardButton('Ногти', callback_data='Nails')
inline_btn6 = InlineKeyboardButton('Волосы', callback_data='Hair')
inline_btn7 = InlineKeyboardButton('Ресницы', callback_data='Eyelash')

# Ногти

inline_btn8 = InlineKeyboardButton('Маникюр', callback_data='manicure')
inline_btn9 = InlineKeyboardButton('Педикюр', callback_data='pedicure')