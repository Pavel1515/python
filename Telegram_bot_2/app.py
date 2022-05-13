from config import token
from telebot import types,telebot
from googletrans import Translator
    
bot = telebot.TeleBot(token)
list_en = ['b','d','f','g','h','j','k','l','m','n','q','r','s','t','v','w','z']

@bot.message_handler(content_types = ["text"])
def handler(message):
    y = message.text
    b = False
    try:
        for z in str(y.lower()):
            for i in list_en:
                if i == z :
                    Ru_translate(message)
                    m = 10
                    b = True
                    break
            if b == True:
                break
        print(m)
    except:
        Engl_translate(message)


    
@bot.message_handler(content_types = ["text"])             
def Engl_translate(message):
    trans = Translator()
    t = trans.translate(message.text,src = 'ru', dest='en')
    bot.send_message(message.chat.id, t.text)

@bot.message_handler(content_types = ["text"]) 
def Ru_translate(message): 
    trans = Translator()
    t = trans.translate(message.text,dest ='ru')
    bot.send_message(message.chat.id, t.text)
    
if __name__ == '__main__':
     bot.polling()