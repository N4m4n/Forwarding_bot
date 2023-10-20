import telebot
import requests
import json
from telegram.ext import *
API_KEY = '5690531199:AAFAIi1PKU-sixH4DF2y8avyAej4Ia78sXo'
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
    bot.forward_message(-4038457815, -4082924192, message.message_id)
    bot.send_message(-4038457815, message.text)