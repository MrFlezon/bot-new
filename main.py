import requests
import telebot
from telebot import  types

bot = telebot.TeleBot('1499784612:AAFiM9wiDymoK6aGuPvL0HoXLr4laOeFfwc')

keyboard = types.InlineKeyboardMarkup()

key_news_polit = types.InlineKeyboardButton(text="ШО творится В нашем МИРЕ", callback_data='polit')
keyboard.add(key_news_polit)

key_news_covid = types.InlineKeyboardButton(text="Каранавирус, Карона УХАДИ С НАШЕГО РАЙОНА", callback_data='covid')
keyboard.add(key_news_covid)

key_news_it = types.InlineKeyboardButton(text="Я У МАМЫ ПРОГРАМИСТ", callback_data='it')
keyboard.add(key_news_it)

key_news_weather = types.InlineKeyboardButton(text="НАДО выглянуть в окно", callback_data='weather')
keyboard.add(key_news_weather)

key_news_youtube = types.InlineKeyboardButton(text="Ютупчик", callback_data='youtube')
keyboard.add(key_news_youtube)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'youtube':
        bot.send_message(call.message.chat.id, "https://www.youtube.com/")
    elif call.data == 'weather':
        weather = requests.get('https://wttr.in/Moscow?format=3')
        bot.send_message(call.message.chat.id, weather)

    else:
        bot.send_message(call.message.chat.id, "Хочешь Больше Дай Больше Денег")


@bot.message_handler(content_types=['text'])
def get_text_message(message):

    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Дароу")
        bot.send_message(message.from_user.id, "А ШО ТОБЕ НАДО?", reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "слышь ты писать привет только с большой буквы!!! ТЫ МЕНЯ ПОНЯЛ??")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понял БЫСТРО НАПИСАЛ /help")



bot.polling(none_stop=True, interval=0)