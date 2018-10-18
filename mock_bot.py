from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from spongemock import spongemock
import random
import os

TOKEN = "bot token"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("/mock to to mock someone")


@dp.message_handler(commands=['mock'])
async def mock(message: types.Message):
    if message.reply_to_message:
        origtext = message.reply_to_message.text
        mocked = spongemock.mock(origtext)
        randint = random.randint(1, 699)
        magick = """magick bob.jpg -font Impact -pointsize 50 -size 800x450 -stroke black -strokewidth 3 -fill white -background none -gravity north caption:"{}" -flatten mocked{}.jpg""".format(mocked, randint)
        os.system(magick)
        with open('mocked{}.jpg'.format(randint), 'rb') as mockedphotu:
            await message.reply_to_message.reply_photo(photo=mockedphotu, reply=message.reply_to_message)
        os.remove('mocked{}.jpg'.format(randint))
    else:
        message.reply('kensur content type beesh')

if __name__ == '__main__':
    executor.start_polling(dp)
