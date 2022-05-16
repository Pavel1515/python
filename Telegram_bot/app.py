from gc import callbacks
from importlib.resources import contents
from msilib.schema import tables
from sqlite3 import connect
from traceback import print_tb
from unicodedata import name
from config import TOKEN , api_keys, UTC0530
from datetime import tzinfo, timedelta, datetime, timezone
from telebot import types,telebot
import requests
import sqlite3


bot = telebot.TeleBot(TOKEN)


markup_reaply = types.ReplyKeyboardMarkup(resize_keyboard= True)
item_city = types.KeyboardButton("Последний поиск")
markup_reaply.add(item_city)


@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id,"Приветствую этот бот показует погоду , тут можно  сохранить город и потом обновлять ", reaply_makup = markup_reaply )


def my_city(message):
    db = sqlite3.connect('Telegram_bot\sql.db')
    cursor = db.cursor()
    id  = [message.chat.id] 
    r = cursor.execute("SELECT city FROM user WHERE id=?",id).fetchone()
    city = r[0]
    times= datetime.now(UTC0530())  
    times = times.strftime("%H:%M")
    api  = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_keys}&units=metric"
    res = requests.get(api)
    data= res.json()
    name = data['name']
    temp = int(data['main']['temp'])
    fleels_like = int(data['main']['feels_like'])
    conntry = data['sys']['country']
    bot.send_message(message.chat.id, f"\U0001F3E1 \U0001F3E1 \U0001F3E1Город:  {name}\
    \nТемпература: {temp} ℃\nОщущение: {fleels_like } ℃\
    \n\U0001F680Страна:\U0001F680{conntry}\
    \nВремя: {times}" , reply_markup = markup_reaply)
    db.close()


def save(table ,table_1): 
    try:
        db = sqlite3.connect('sql\sql.db')
        cursor = db.cursor()
        cursor.execute('INSERT INTO user VALUES(?,?)',table)
        db.commit()
        db.close()
    except:
        db = sqlite3.connect('sql\sql.db')
        cursor = db.cursor()
        cursor.execute('UPDATE user SET city ==? WHERE id ==?',table_1)
        db.commit()
        db.close()


@bot.message_handler(content_types=["text"])
def repetrear(message):
    if message.text == "Последний поиск":
        my_city(message)
    else:
        try:
            times= datetime.now(UTC0530())  
            times = times.strftime("%H:%M")
            res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={api_keys}&units=metric")
            data= res.json()
            name = data['name']
            temp = int(data['main']['temp'])
            fleels_like = int(data['main']['feels_like'])
            conntry = data['sys']['country']
            bot.send_message(message.chat.id, f"\U0001F3E1 \U0001F3E1 \U0001F3E1Город:  {name}\
            \nТемпература: {temp} ℃\nОщущение: {fleels_like } ℃\
            \n\U0001F680Страна:\U0001F680{conntry}\
            \nВремя: {times}" , reply_markup = markup_reaply)
            table = [message.from_user.id ,message.text]
            table_1 = [message.text, message.from_user.id]
            save(table ,table_1)
        except:
            bot.send_message(message.chat.id, " Введите правильно город ")

if __name__ == '__main__':
     bot.infinity_polling()