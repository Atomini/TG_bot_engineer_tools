import asyncio
from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types
import logging

loop = asyncio.get_event_loop()
bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)


if __name__ == '__main__':
    from heandlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin, skip_updates=True)