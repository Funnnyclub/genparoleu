import random

import requests
import datetime
from config import tg_tolen
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token = tg_tolen)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await  message.reply("Привет, напиши количество символов для пароля: ")


@dp.message_handler()
async def get_weather(message: types.Message):
    sumbyl = message.text
    pas = ''
    try:
        for x in range(int(sumbyl)): #Количество символов (16)
            pas = pas + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ')) #Символы, из которых будет составлен пароль
        await message.reply(f'Твой, новый пароль: {pas}')
    except:
       await message.reply("Проверьте название города")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    executor.start_polling(dp)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
