#!venv/bin/python
from ntpath import join
from re import split
import config
import telebot
from telebot import types
import requests



city = "Odessa"
api  = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={config.api_keys}"

res = requests.get(api)
k = str(res.json())


lat,lon = config.character_exclusion(k) 



















# bot = telebot.TeleBot(config.TOKEN)
# ma2`rkup = types.ReplyKeyboardMarkup(resize_keyboard=True)


# item_1 = types.KeyboardButton(text="Погода")
# item_2 = types.KeyboardButton(text="Инфо")
# markup.add(item_1,item_2)



# @bot.message_handler(content_types=["text"])
# def privet(message):
#     if message.text == "P":
#         r = open("Telegram_bot/sticers/AnimatedSticker.tgs", "rb")
#         bot.send_sticker(message.chat.id, r , reply_markup=markup)
#     else:
#         bot.send_message(message.chat.id, "Несработало", reply_markup=markup)



# @bot.message_handler(content_types=["text"])
# def repetrear(message):
#     bot.send_message(message.chat.id, "Привет")
# if __name__ == '__main__':
#      bot.infinity_polling()