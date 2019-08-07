import telebot
from telebot import apihelper

apihelper.proxy = {'https':'socks5://Naatkok:jGgTzR7kvzIFpdReXcrd22V15MfHtDOKdSUbWXgH@vpnzone.technology:10580'}

bot = telebot.TeleBot(' '); #здесь ключ от робота

import weather_func

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я могу подсказать тебе прогноз погоды на сегодня. Введи город, где хочешь узнать прогноз.')

@bot.message_handler(content_types=['text'])

def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет! В каком городе хочешь узнать погоду?')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'До новых встреч')
    else:
        weather = weather_func.get_tempereture(message.text)
        if weather == None:
            bot.send_message(message.chat.id, 'Извини, ничего не могу найти. Введи только город в котором ты хочешь узнать погоду в именительном падеже.')
        else:
            bot.send_message(message.chat.id, 'погода в твоем городе ' + str(weather) + 'градусов')

bot.polling(none_stop=True, interval=0)