from config import TOKEN , api_keys, UTC0530
from datetime import tzinfo, timedelta, datetime, timezone
from telebot import types,telebot
import requests


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types = ["text"])
def message_start(message):
    if  message.text == "/start":
        bot.send_message(message.chat.id , "Вітаю цей бот показуе погоду та час")
    else:
        repetrear(message)

@bot.message_handler(content_types=["text"])
def repetrear(message):
    try:
        times= datetime.now(UTC0530())  
        times = times.strftime("%H:%M")
        valuta  = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
        valuta = valuta.json()
        USD  = valuta[25]["rate"]
        EUR = valuta[32]["rate"]
        PLN  = valuta[33]["rate"]
        api  = f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={api_keys}&units=metric"
        res = requests.get(api)
        data= res.json()
        name = data['name']
        temp = int(data['main']['temp'])
        fleels_like = int(data['main']['feels_like'])
        conntry = data['sys']['country']
        bot.send_message(message.chat.id, f"\U0001F3E1 \U0001F3E1 \U0001F3E1Город:  {name}\
        \nТемпература: {temp} ℃\nОщущение: {fleels_like } ℃\
        \n\U0001F680Страна:\U0001F680{conntry}\
        \nВремя: {times}")
    except:
        bot.send_message(message.chat.id, " Введите правильно город ")

if __name__ == '__main__':
     bot.infinity_polling()