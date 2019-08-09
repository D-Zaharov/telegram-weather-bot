import telebot
from telebot import apihelper

apihelper.proxy = {'https':'socks5h://Naatkok:jGgTzR7kvzIFpdReXcrd22V15MfHtDOKdSUbWXgH@vpnzone.technology:10580'}

import keys

bot = telebot.TeleBot(keys.bot);

import weather_func

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Я могу дать тебе информацию о погоде в городе, который ты выберешь. Напиши сначала тип данных, который хочешь получить и затем название города. Пока доступны три варианта: Скорость ветра, Температура, Погодные условия.')

@bot.message_handler(content_types=['text'])

def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет! В каком городе хочешь узнать погоду?')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'До новых встреч')
<<<<<<< HEAD
    elif message.text.lower()[:11] == 'температура':
        weather = weather_func.get_tempereture(keys.api, message.text)
        if weather == None:
            bot.send_message(message.chat.id, 'Извини, ничего не могу найти.')
        else:
            bot.send_message(message.chat.id, 'Температура в выбранном городе ' + str(weather) + 'градусов')
    elif message.text.lower()[:14] == 'скорость ветра':
        weather = weather_func.get_wind(keys.api, message.text)
=======
    else:
        weather = weather_func.get_tempereture(keys.api, message.text)
>>>>>>> 5b0ed8dc17bb9ba7bce20e62a1d47d1107b4117e
        if weather == None:
            bot.send_message(message.chat.id, 'Извини, ничего не могу найти.')
        else:
            bot.send_message(message.chat.id, 'Скорость ветра в выбранном городе ' + str(weather) + 'метров в секунду')
    elif message.text.lower()[:16] == 'погодные условия':
        weather = weather_func.get_details(keys.api, message.text)
        if weather == None:
            bot.send_message(message.chat.id, 'Извини, ничего не могу найти.')
        else:
            bot.send_message(message.chat.id, 'Погодные условия в выбранном городе: ' + str(weather))
    else:
        bot.send_message(message.chat.id, 'Не соблюдён формат!')

bot.polling(none_stop=True, interval=0)