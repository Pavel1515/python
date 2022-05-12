from config import token
from telebot import types,telebot
from googletrans import Translator
    
bot = telebot.TeleBot(token)

@bot.message_handler(content_types = ["text"])
def handler(message):
    list_en = ['b','d','f','g','h','j','k','l','m','n','q','r','s','t','v','w','x','z']
    for z in message.text.lower():
        for i in list_en:
            if z == i:
                Ru_translate(message)
            else:
                Engl_translate(message)
            break

def Ru_translate(message): 
    trans = Translator()
    t = trans.translate(message.text)
    bot.send_message(message.chat.id, t.text)
             
def Engl_translate(message):
    trans = Translator()
    t = trans.translate(message.text ,dest = 'en')
    bot.send_message(message.chat.id, t.text)

if __name__ == '__main__':
     bot.polling()