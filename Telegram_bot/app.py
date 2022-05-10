import config
import telebot
from telebot import types
import requests

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types = ["text"])
def message_start(message):
    if  message.text == "/start":
        bot.send_message(message.chat.id , "Вітаю цей бот показуе погоду та час")
    else:
        repetrear(message)


@bot.message_handler(content_types=["text"])
def repetrear(message):
    try:
        api  = f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={config.api_keys}&units=metric"
        res = requests.get(api)
        data= res.json()
        name = data['name']
        temp = int(data['main']['temp'])
        fleels_like = int(data['main']['feels_like'])
        conntry = data['sys']['country']
        bot.send_message(message.chat.id, f"Місто: {name}\nТемпература: {temp} C\nВідчуваеться: {fleels_like } C\nКраїна: {conntry }")
    except:
        bot.send_message(message.chat.id, " Введите правильно город ")




if __name__ == '__main__':
     bot.infinity_polling()