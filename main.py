import telebot
import os

TOKEN = os.environ.get('TOKEN')
CHANNEL_ID = os.environ.get('CHANNEL_ID')

bot = telebot.TeleBot(TOKEN)

bot.send_message(CHANNEL_ID, "البوت يعمل الآن بنجاح! 💪")

print("البوت شغال!")
