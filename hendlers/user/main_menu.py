from aiogram import types
from misc import dp, bot
from keyboards.default import main_keyboards as kb


@dp.message_handler(commands=["start"])
async def start_menu(message: types.Message):
    await bot.send_message(message.from_user.id,text="Главное меню", reply_markup=kb.main_keyboard)


@dp.message_handler(content_types=["text"])
async def mass_menu(message: types.Message):
    if message.text == "Расчет масси":
        await bot.send_message(message.from_user.id, text="Меню массы", reply_markup=kb.mass_keyboard)
    elif message.text == "Расчет геометрии":
        await bot.send_message(message.from_user.id, text="Меню геометрии", reply_markup=kb.geom_keyboard)
