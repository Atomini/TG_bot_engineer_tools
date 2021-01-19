import logging
from aiogram import Bot, Dispatcher
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
loop = asyncio.get_event_loop()  # TODO узнать что делает и как изменить время с 20 сек
bot = Bot(token=str(TOKEN), parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)
logging.basicConfig(level=logging.DEBUG)

