from aiogram import types
from misc import dp, bot
from keyboards.default import main_keyboards as kb



from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from functions.functions import *


class Mydialog(StatesGroup):
    sheet_otvet = State()  # Will be represented in storage as 'Mydialog:otvet'
    cylinder_otvet = State()
    gasket_otvet = State()
    pipe_otvet = State()


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

        await Mydialog.sheet_otvet.set()  # вот мы указали начало работы состояний (states)
        await bot.send_message(message.from_user.id, "Введите данные для расчета в формате\n"
                                                     "длина+ширина+толщина+количество листов+плотность\n"
                                                     "<b>в милиметрах</b>\n"
                                                     "количество листов и плотность вводить не обезательно\n"
                                                     "по умолчанию количество листов = 1\n"
                                                     "плотность = 7850 (сталь)\n")
    elif message.text == "Масса круга":
        await Mydialog.cylinder_otvet.set()
        await bot.send_message(message.from_user.id, "Введите данные для расчета в формате\n"
                                                     "диаметр+длина круга+плотность\n"
                                                     "<b>в милиметрах</b>\n"
                                                     "плотность вводить не обезательно\n"
                                                     "по умолчанию плотность = 7850 (сталь)")
    elif message.text == "Масса прокладки":
        await Mydialog.gasket_otvet.set()
        await bot.send_message(message.from_user.id, "Введите данные для расчета в формате\n"
                                                     "наружный диаметр+внутрений диаметр+толщина+плотность\n"
                                                     "<b>в милиметрах</b>\n"
                                                     "плотность и толщину вводить не обезательно\n"
                                                     "по умолчанию плотность = 2000 (паронит)\n"
                                                     "толщина  = 3 мм")
    elif message.text == "Масса трубы":
        await Mydialog.pipe_otvet.set()
        await bot.send_message(message.from_user.id, "Введите данные для расчета в формате\n"
                                                     "Наружный диаметр+тощина стенки(через точку)"
                                                     "+длина трубы+плотность\n"
                                                     "<b>в милиметрах</b>\n"
                                                     "плотность вводить не обезательно\n"
                                                     "плотность = 7850 (сталь)\n")


@dp.message_handler(state=Mydialog.pipe_otvet)
async def pipe_message(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
        user_message = data['text']
        if user_message == "End":
            await state.finish()
        else:
            answer = input_data(user_message)
            final_answer = weight_pipe(*answer)
            await bot.send_message(message.from_user.id, text="{}\nДля завершения наберите End".format(final_answer))


@dp.message_handler(state=Mydialog.gasket_otvet)
async def gasket_message(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
        user_message = data['text']
        if user_message == "End":
            await state.finish()
        else:
            answer = input_data(user_message)
            final_answer = weight_gasket(*answer)
            await bot.send_message(message.from_user.id, text="{}\nДля завершения наберите End".format(final_answer))


@dp.message_handler(state=Mydialog.cylinder_otvet)
async def cylinder_message(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
        user_message = data['text']
        if user_message == "End":
            await state.finish()
        else:
            answer = input_data(user_message)
            final_answer = weight_cylinder(*answer)
            await bot.send_message(message.from_user.id, text="{}\nДля завершения наберите End".format(final_answer))


@dp.message_handler(state=Mydialog.sheet_otvet)
async def sheet_message(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
        user_message = data['text']
        if user_message == "End":
            await state.finish()
        else:
            answer = input_data(user_message)
            final_answer = weight_sheet(*answer)

            await bot.send_message(message.from_user.id, text="{}\nДля завершения наберите End".format(final_answer))
    # Finish conversation
    # await state.finish()  # закончили работать с сотояниями
            await Mydialog.sheet_otvet.set()

