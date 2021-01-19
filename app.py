from aiogram import executor
from misc import dp
import hendlers


if __name__ == '__main__':

    executor.start_polling(dp, on_startup=hendlers.admin.send_to_admin,
                           skip_updates=True)
