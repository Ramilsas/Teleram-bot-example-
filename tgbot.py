import telebot
from telebot import types
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Напиши или нажми: /help для продолжения!')


@bot.message_handler(commands=['help'])
def social_media(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button1 = types.KeyboardButton('Соц сети')
    button2 = types.KeyboardButton('Аватарки для ноября')
    markup.add(button1)
    markup.add(button2)
    bot.send_message(message.chat.id,"Выберите что вам нужно", reply_markup=markup)


@bot.message_handler()
def photo(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Instagram", url='https://www.instagram.com/ramil_btw/'))
    markup.add(types.InlineKeyboardButton("VKontakte", url='https://vk.com/sas_rambl4'))
    markup.add(types.InlineKeyboardButton("Twitch", url='https://www.twitch.tv/zxc_rambl4'))
    markup.add(types.InlineKeyboardButton("FACEIT", url='https://www.faceit.com/ru/players/Rambl4'))
    markup.add(types.InlineKeyboardButton("Telegram Group", url='https://t.me/+3p6p-Itdg-8wNDBi'))
    if message.text == "Соц сети":
        bot.send_message(message.chat.id,"Подпишись на мои соц сети :)", reply_markup=markup)
    elif message.text == 'Аватарки для ноября':
        photo = open('jedi.jpg', 'rb')
        photo1 = open('sith.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_photo(message.chat.id, photo1)
    else:
        bot.send_message(message.chat.id, 'Перезапустите бота при помощи команды /start')