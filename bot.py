user_data = {}

import telebot
from telebot import types

bot = telebot.TeleBot('YOUR_TOKEN_HERE')

bsm = bot.send_message
tkb = types.KeyboardButton
tikb = types.InlineKeyboardButton

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btnst = tkb('Press me to start')
    markup.row(btnst)
    bsm(message.chat.id, 'Press button to start!', reply_markup=markup)


def main(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = tkb('View Menu')
    btn2 = tkb('My order')
    btn3 = tkb('Clear cart')
    btn4 = tkb('Delivery')
    btn5 = tkb('Help / Contact')
    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn3, btn4)
    markup.row(btn5)
    bot.send_message(message.chat.id, 'Hello! This is main menu', reply_markup=markup)

def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_pizza = tkb('Pizza')
    btn_burger = tkb('Burger')
    btn_french = tkb('French fries')
    btn_rybeye = tkb('Rybeye')
    back = tkb('Back to main')
    markup.add(btn_pizza, btn_burger)
    markup.add(btn_french, btn_rybeye)
    markup.add(back)
    bsm(message.chat.id, 'Menu:', reply_markup=markup)

def dev(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    location_btn = tkb('Send my location', request_location=True)
    back = tkb('Back to main')
    markup.add(location_btn)
    markup.add(back)
    bsm(message.chat.id, 'Please share your location for delivery:', reply_markup=markup)

@bot.message_handler(content_types=['location'])
def locat(message):
    if message.location:
        latitude = message.location.latitude
        longitude = message.location.longitude
        bsm(message.chat.id, f"Thanks! We received your location:\nLatitude: {latitude}\nLongitude: {longitude}")
    else:
        None
        
def help(message):
    bsm(message.chat.id, "This bot was made for my portfolio. \n Author: J4m80")

@bot.message_handler(func=lambda message: True)
def logic(message):
    chat_id = message.chat.id
    text = message.text

    if text == 'View Menu':
        menu(message)
    elif text == 'Delivery':
        dev(message)
    elif text == 'Press me to start':
        main(message)
    elif text == 'Back to main':
        main(message)
    elif text == 'Help / Contact':
        help(message)

    elif text in ['Pizza', 'Burger', 'French fries', 'Rybeye']:
        if chat_id not in user_data:
            user_data[chat_id] = {'cart': []}
        user_data[chat_id]['cart'].append(text)
        bsm(chat_id, f'✅ {text} added to your cart!')

    elif text == 'My order':
        cart_items = user_data.get(chat_id, {}).get('cart', [])
        if cart_items:
            items = '\n'.join(f"{i+1}. {item}" for i, item in enumerate(cart_items))
            bsm(chat_id, f'🛒 Your cart:\n{items}\n\nTo remove an item, type its number (e.g. 2)')
        else:
            bsm(chat_id, '🛒 Your cart is empty!')

    elif text == 'Clear cart':
        user_data[chat_id] = {'cart': []}
        bsm(chat_id, '🧹 Your cart has been cleared!')

    elif text.isdigit():
        cart = user_data.get(chat_id, {}).get('cart', [])
        index = int(text) - 1
        if 0 <= index < len(cart):
            removed = cart.pop(index)
            bsm(chat_id, f'❌ {removed} removed from your cart!')
        else:
            bsm(chat_id, '⚠️ Invalid number! Try again.')


bot.polling(none_stop=True)
