import telebot

bot = telebot.TeleBot('5894901208:AAGjS2I0_dCurNpq0zv9E6mcZKJQ74PBOj8')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('hello','bye')

@bot.message_handler(commands=['start'])

def start_message(message):
    bot.send_message(message.chat.id, 'Hello, can I help?', reply_markup=keyboard1)
    
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'hello':
        bot.send_message(message.chat.id, 'And you hello!')
    elif message.text == 'bye':
        bot.send_message(message.chat.id, 'Bye!')
    else:
        bot.send_message(message.chat.id, 'WHAT?!')

bot.polling()