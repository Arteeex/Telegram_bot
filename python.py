import telebot;
bot = telebot.TeleBot('7766184419:AAHWwB5I6VWbZIbGN4guYDi4VwtG3WVjWzM');
import time
from datetime import datetime

time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, datetime.now().hour, datetime.now().minute)
    if time.hour == <01> and time.minute == <07>:
        await bot.send_message(message.from_user.id, f'Время: {time.hour}:{time.minute}')
    else: 
        await bot.send_message(message.from_user.id, time)


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help")

bot.polling(none_stop=True, interval=0)
