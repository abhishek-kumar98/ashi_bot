import datetime

import telebot
from time import time, sleep
from datetime import timezone

bot = telebot.TeleBot("5086776971:AAEmqDzuPnIrx73uT4MvGsAXz0QwdEuoID8", parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hey my love! Here is a bot to remind you to drink water and take your meds/vitamins! "
                          "\U0001F9E1")

    while True:
        sleep(1800 - time() % 1800)
        bot.send_message(message.chat.id, "It's time to drink water, my love! \U0001F6B0 \n \n Abhi loves you so much "
                                          "\U0001F97A\U0001F9E1 ")

        dt_now = datetime.datetime.now(datetime.timezone.utc)
        print(dt_now)
        if dt_now.hour == 4 and dt_now.minute <= 30:
            bot.send_message(message.chat.id,
                             "It's time to take your morning medicines, my love! \uE30F \n \n Abhi loves you so much "
                             "\U0001F97A\U0001F9E1 ")

        elif dt_now.hour == 4:
            bot.send_message(message.chat.id,
                             "Another reminder to take your morning medicines, my love! \uE30F \n \n Abhi loves you so much "
                             "\U0001F97A\U0001F9E1 ")

        elif dt_now.hour == 9 and dt_now.minute <= 30:
            bot.send_message(message.chat.id,
                             "It's time to take your afternoon vitamins, my love! \uE30F \n \n Abhi loves you so much "
                             "\U0001F97A\U0001F9E1 ")

        elif dt_now.hour == 9:
            bot.send_message(message.chat.id,
                             "Another reminder to take your afternoon vitamins, my love! \uE30F \n \n Abhi loves you so much "
                             "\U0001F97A\U0001F9E1 ")

        elif dt_now.hour == 18 and dt_now.minute <= 30:
            bot.send_message(message.chat.id,
                             "It's time to take your night medicines, my love! \uE30F \n \n Abhi loves you so much "
                             "\U0001F97A\U0001F9E1 ")

        elif dt_now.hour == 18:
            bot.send_message(message.chat.id,
                             "Another reminder to take your night medicines, my love! \uE30F \n \n Abhi loves you so much "
                             "\U0001F97A\U0001F9E1 ")


bot.infinity_polling()
