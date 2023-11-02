import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import requests

api = "http://api.open-notify.org/iss-now.json"

botToken = "Your Bot Token"

bot = telebot.TeleBot(botToken)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    data = call.data
    if data == 'update':
        i1 = [[InlineKeyboardButton(text=f'Check Now',
     callback_data=f'update')]]
        inline_keyboard = InlineKeyboardMarkup(i1)
        issPosition = requests.get(api).json()["iss_position"]
        latitude, longitude = issPosition['latitude'], issPosition['longitude']
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_location(call.message.chat.id, latitude, longitude, reply_markup=inline_keyboard)

@bot.message_handler(commands=['start'])
def start(message):
    try:
        issPosition = requests.get(api).json()["iss_position"]
        latitude, longitude = issPosition['latitude'], issPosition['longitude']
        i1 = [[InlineKeyboardButton(text=f'Check Now',
     callback_data=f'update')]]
        inline_keyboard = InlineKeyboardMarkup(i1)
        bot.send_message(message.chat.id,
         f"Current ISS Location")
        bot.send_location(message.chat.id, latitude, longitude, reply_markup=inline_keyboard)
    except Exception:
        bot.send_message(message.chat.id,
         f"Unable To Generate Image")



bot.infinity_polling()
#https://www.facebook.com/zerocruch/
#https://tiktok.com/@zerocruch
#https://www.youtube.com/@zerocruch
#https://www.instagram.com/zerocruch_
