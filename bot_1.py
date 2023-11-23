import os

import telebot
from telebot import types

import random
from random import choice

#BOT_TOKEN = os.environ.get("6524527794:AAFbilp4sVUrwEdqVqDSAf_IzGZ_nFv4ggY")

bot = telebot.TeleBot("6524527794:AAFbilp4sVUrwEdqVqDSAf_IzGZ_nFv4ggY")

spacefacts = ['Asenal chempin']


@bot.message_handler(commands=['start'])
def send_welcome(message):
    #bot.send_message(message.chat.id, f'Привіт, {message.from_user.first_name} {message.from_user.last_name}') 🇬🇧🇺🇦
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🇺🇦 Українська')
    btn2 = types.KeyboardButton('🇬🇧 English')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "🇺🇦 Виберіть мову / 🇬🇧 Choose your language", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    #Українська мова
    if message.text == '🇺🇦 Українська':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🇺🇦 Українська спорт")
        btn2 = types.KeyboardButton('📰 Новини')
        btn3 = types.KeyboardButton('📁 Заходи')
        btn4 = types.KeyboardButton('📚 Знання')
        btn5 = types.KeyboardButton('💻 Навігація посилань')
        btn6 = types.KeyboardButton('👩🏻‍🏫 Скіли')
        btn7 = types.KeyboardButton('🎬 Відео')
        btn8 = types.KeyboardButton('🔎 Пошук')
        btn9 = types.KeyboardButton('👀 Цікавинка!')
        btn10 = types.KeyboardButton('🔙 Повернутись до вибору мови')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)
        bot.send_message(message.from_user.id, "👋 вітає на спорт аналітік", reply_markup=markup)
        bot.send_message(message.from_user.id, '👀 Вибіріть тематику')

    elif message.text == '🔙 Повернутись до вибору мови':
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         btn1 = types.KeyboardButton('🇺🇦 Українська')
         btn2 = types.KeyboardButton('🇬🇧 English')
         markup.add(btn1, btn2)
         bot.send_message(message.from_user.id, "🇺🇦 Виберіть мову / 🇬🇧 Choose your language", reply_markup=markup)

    elif message.text == '👀 Цікавинка!':
        for i in range(10):
            bot.send_message(message.from_user.id, random.choice(spacefacts))


#bot.polling(none_stop=True)
    

