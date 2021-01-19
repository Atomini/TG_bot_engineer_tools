from aiogram import types
from misc import dp, bot
from keyboards.default import main_keyboards as kb

#---------------------test-------------------------------------------------

from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from functions.functions import *
class Mydialog(StatesGroup):
    otvet = State()  # Will be represented in storage as 'Mydialog:otvet'


#-----------------------test-----------------------------------------------



@dp.message_handler(commands=["start"])
async def start_menu(message: types.Message):
    await bot.send_message(message.from_user.id, text="Главное меню", reply_markup=kb.main_keyboard)


@dp.message_handler(content_types=["text"])
async def mass_menu(message: types.Message):
    if message.text == "Расчет масси":
        await bot.send_message(message.from_user.id, text="Меню массы", reply_markup=kb.mass_keyboard)
    elif message.text == "Главное меню":
        await bot.send_message(message.from_user.id, text="Главное меню", reply_markup=kb.main_keyboard)
    elif message.text == "Расчет геометрии":
        await bot.send_message(message.from_user.id, text="Меню геометрии", reply_markup=kb.geom_keyboard)
    elif message.text == "Масса листа":
        # ----------------------------test------------------------------------------
        await Mydialog.otvet.set()  # вот мы указали начало работы состояний (states)
        # -----------------------------test-----------------------------------------
        await bot.send_message(message.from_user.id, "ВВедите размеры листа в формате a+b+c") #TODO написать нормальное описание


#---------------------------test-------------------------------------------
@dp.message_handler(state=Mydialog.otvet)
async def process_message(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
        user_message = data['text']
        answer = input_data(user_message)

        answer_1 = weight_sheet(*answer)

        await bot.send_message(message.from_user.id, answer_1)

    # Finish conversation
    await state.finish()  # закончили работать с сотояниями

#-----------------------------test-----------------------------------------
