import logging
from aiogram import Bot, Dispatcher
from config import TOKEN
import asyncio

loop = asyncio.get_event_loop()  # TODO узнать что делает и как изменить время с 20 сек
bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)
logging.basicConfig(level=logging.DEBUG)
