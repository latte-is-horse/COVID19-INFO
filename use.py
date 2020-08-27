# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 23:08:08 2020

@author: comks
"""


import os

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN', '')
CHAT_ID = os.environ.get('CHAT_ID', '')

if not TELEGRAM_TOKEN or not CHAT_ID:
  raise Exception('TELEGRAM_TOKEN, CHAT_ID 확인필요')