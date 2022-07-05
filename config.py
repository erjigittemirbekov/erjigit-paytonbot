import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
from decouple import config

TOKEN = config("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())
ADMIN = 1163755303
URL = "https://dashboard.heroku.com/apps/bot-erjigit/logs"
URI = "postgres://bqtdfusatkatgv:27d29bb5a40af944fad42b7d491aacf5a35194adb6cf29106c831f3c85409627@ec2-52-212-228-71.eu-west-1.compute.amazonaws.com:5432/d6v79tvbdovk13"