import logging
from aiogram import Bot, Dispatcher
import os
import asyncio
from dotenv import load_dotenv



#-----------test--------------------------
from aiogram.contrib.fsm_storage.memory import MemoryStorage
storage = MemoryStorage()
#-----------test--------------------------


load_dotenv()
TOKEN = os.getenv("TOKEN")
loop = asyncio.get_event_loop()  # TODO узнать что делает и как изменить время с 20 сек
bot = Bot(token=str(TOKEN), parse_mode="HTML", )
dp = Dispatcher(bot, loop=loop, storage=storage)    # add ---> , storage=storage
logging.basicConfig(level=logging.DEBUG)

