# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 23:07:27 2020

@author: comks
"""


from use import TELEGRAM_TOKEN, CHAT_ID
import requests as rq
import telegram 

bot = telegram.Bot(token=TELEGRAM_TOKEN)

def send(t):
  bot.sendMessage(CHAT_ID, t, parse_mode=telegram.ParseMode.HTML)