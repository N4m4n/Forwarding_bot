import os
from telebot import types
import telebot
import requests
import json

API_KEY = '5690531199:AAFAIi1PKU-sixH4DF2y8avyAej4Ia78sXo'
print("started")
# print(API_KEY)
bot = telebot.TeleBot(API_KEY, parse_mode=None)



def checkIfGroup(message):
	# if message.chat.type == 'group' or message.chat.type == 'supergroup':
    return True




def call():

    updates = requests.get('http://api.telegram.org/bot5690531199:AAFAIi1PKU-sixH4DF2y8avyAej4Ia78sXo/getUpdates')
    if updates.status_code ==200:
        data = json.loads(updates.text)
        last = data['result'][-1]
        ide = ''
        if 'photo' in last['message']:
            foto = True
            ide = last['message']['photo'][2]['file_id']
        else:
            foto = False
            print('no photo')
        return foto, ide

@bot.message_handler(func=checkIfGroup)
def sendGrpMessage(message):
	print(message.chat.id)
	print(message)  
	bot.forward_message(-4038457815, -4082924192, message.message_id)
     	
	


bot.infinity_polling()