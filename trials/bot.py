import telebot
import requests
import json
from telegram.ext import *
API_KEY = '5179844705:AAGsInH-Jf7PmKT3MQx32plvWmtyaayEXxU'
# print("started")
# # print(API_KEY)
bot = telebot.TeleBot(API_KEY, parse_mode=None)

def checkIfGroup(message):
	# if message.chat.type == 'group' or message.chat.type == 'supergroup':
    return True


@bot.message_handler(func=checkIfGroup)
def sendGrpMessage(message):
    print(message.chat.id)
    print(message)

bot.polling()