from aiogram import types
from misc import dp, bot
from keyboards.default import main_keyboards as kb

from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from functions.functions import *


class MyDialog(StatesGroup):
    sheet_otvet = State()  # Will be represented in storage as 'Mydialog:otvet'
    cylinder_otvet = State()
    gasket_otvet = State()
    pipe_otvet = State()
    bottom_otvet = State()
    cylinder_sweep_otvet = State()
    bottom_perimeter_sweep_otvet = State()
    height_cylindrical_part_otvet = State()
    volume_cylindrical_part_otvet = State()
    tank_volume_otvet = State()


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

        await MyDialog.sheet_otvet.set()  # вот мы указали начало работы состояний (states)
        await bot.send_message(message.from_user.id, "Введите данные для расчета в формате\n"
                                                     "длина+ширина+толщина+количество листов+плотность\n"
                                                     "<b>в милиметрах</b>\n"
                                                     "количество листов и плотность вводить не обезательно\n"
                                                     "по умолчанию количество листов = 1\n"
                                                     "плотность = 7850 (сталь)\n")
    elif message.text == "Масса круга":
        await MyDialog.cylinder_otvet.set()
        await bot.send_message(message.from_user.id, "Введите данные для расчета в формате\n"
                                                     "диаметр+длина круга+плотность\n"
                                                     "<b>в милиметрах</b>\n"
                                                     "плотность вводить не обезательно\n"
                                                     "по умолчанию плотность = 7850 (сталь)")
    elif message.text == "Масса прокладки":
        await MyDialog.gasket_otvet.set()
        await bot.send_message(message.from_user.id, "Введите данные для расчета в формате\n"
                                                     "наружный диаметр+внутрений диаметр+толщина+плотность\n"
                                                     "<b>в милиметрах</b>\n"
                                                     "плотность и толщину вводить не обезательно\n"
                                                     "по умолчанию плотность = 2000 (паронит)\n"
                                                     "толщина  = 3 мм")
    elif message.text == "Масса трубы":
        await MyDialog.pipe_otvet.set()
        await bot.send_message(message.from_user.id, "Введите данные для расчета в формате\n"
                                                     "Наружный диаметр+тощина стенки(через точку)"
                                                     "+длина трубы+плотность\n"
                                                     "<b>в милиметрах</b>\n"
                                                     "плотность вводить не обезательно\n"
                                                     "плотность = 7850 (сталь)\n")
    elif message.text == "Расчет днища":
        await MyDialog.bottom_otvet.set()
        await bot.send_message(message.from_user.id, "Введите данные для расчета в формате\n"
                                                     "внутрений диаметр+высота целиндрической части+толщина стенки+"
                                                     "коефициент елептичности(через точку)+плотность\n"
                                                     "<b>в милиметрах</b>\n"
                                                     "плотность и коефициент вводить не обезательно\n"
                                                     "по умолчанию плотность = 7850 (сталь)\n"
                                                     "коефициент елептичности = <b>0,25</b>")

    elif message.text == "Расчет развертки по средней линни":
        await MyDialog.cylinder_sweep_otvet.set()
        await bot.send_message(message.from_user.id, "Введите данные для расчета в формате\n"
                                                     "внутрений диаметр+толщина стенки\n"
                                                     "<b>в милиметрах</b>")

    elif message.text == "Разчет длини развертки по периметру":
        await MyDialog.bottom_perimeter_sweep_otvet.set()
        await bot.send_message(message.from_user.id, "Введите данные для расчета в формате\n"
                                                     "периметр днища+толщина стенки\n"
                                                     "<b>в милиметрах</b>")

    elif message.text == "Висота цилендрической части":
        await MyDialog.height_cylindrical_part_otvet.set()
        await bot.send_message(message.from_user.id, "Введите данные для расчета в формате\n"
                                                     "висоты цилендрической части+внутренний диаметр\n"
                                                     "<b>в m3+милиметрах</b>")

    elif message.text == "Объем цилендрической части":
        await MyDialog.volume_cylindrical_part_otvet.set()
        await bot.send_message(message.from_user.id, "Введите данные для расчета в формате\n"
                                                     "внутренний диаметр+высота целендрической части\n"
                                                     "<b>в милиметрах</b>")

    elif message.text == "Объем резервууара":
        await MyDialog.tank_volume_otvet.set()
        await bot.send_message(message.from_user.id, "Введите данные для расчета в формате\n"
                                                     "внутренний диаметр+высота целендрической части+"
                                                     "высота целендрической части днища+коэффициент эллиптичности\n"
                                                     "<b>в милиметрах</b>\n"
                                                     "коефициент вводить не обезательно\n"
                                                     "по умолчанию коефициент елептичности = <b>0,25</b>")
    elif message.text == "Таблица снятия усиления":
        await bot.send_message(message.from_user.id, "1600\n" # TODO заполнить динними
                                                     "1800\n"
                                                     "2000\n"
                                                     "2200\n"
                                                     "2400\n"
                                                     "2600\n"
                                                     "2800\n"
                                                     "3000\n"
                                                     "3200\n"
                                                     "3200(0.2)\n")


@dp.message_handler(state=MyDialog.tank_volume_otvet)
async def tank_volume_message(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
        user_message = data['text']
        if user_message == "End":
            await state.finish()
        else:
            answer = input_data(user_message)
            final_answer = tank_volume(*answer)
            await bot.send_message(message.from_user.id, text="{}\nДля завершения наберите End".format(final_answer))


@dp.message_handler(state=MyDialog.volume_cylindrical_part_otvet)
async def volume_cylindrical_part_message(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
        user_message = data['text']
        if user_message == "End":
            await state.finish()
        else:
            answer = input_data(user_message)
            final_answer = volume_cylindrical_part(*answer)
            await bot.send_message(message.from_user.id, text="{}\nДля завершения наберите End".format(final_answer))


@dp.message_handler(state=MyDialog.height_cylindrical_part_otvet)
async def height_cylindrical_part_message(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
        user_message = data['text']
        if user_message == "End":
            await state.finish()
        else:
            answer = input_data(user_message)
            final_answer = height_cylindrical_part(*answer)
            await bot.send_message(message.from_user.id, text="{}\nДля завершения наберите End".format(final_answer))


@dp.message_handler(state=MyDialog.bottom_perimeter_sweep_otvet)
async def bottom_perimeter_sweep_message(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
        user_message = data['text']
        if user_message == "End":
            await state.finish()
        else:
            answer = input_data(user_message)
            final_answer = bottom_perimeter_sweep(*answer)
            await bot.send_message(message.from_user.id, text="{}\nДля завершения наберите End".format(final_answer))


@dp.message_handler(state=MyDialog.cylinder_sweep_otvet)
async def cylinder_sweep_message(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
        user_message = data['text']
        if user_message == "End":
            await state.finish()
        else:
            answer = input_data(user_message)
            final_answer = cylinder_sweep(*answer)
            await bot.send_message(message.from_user.id, text="{}\nДля завершения наберите End".format(final_answer))


@dp.message_handler(state=MyDialog.bottom_otvet)
async def bottom_message(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
        user_message = data['text']
        if user_message == "End":
            await state.finish()
        else:
            answer = input_data(user_message)
            final_answer = calculation_bottom(*answer)
            await bot.send_message(message.from_user.id, text="{}\nДля завершения наберите End".format(final_answer))


@dp.message_handler(state=MyDialog.pipe_otvet)
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


@dp.message_handler(state=MyDialog.gasket_otvet)
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


@dp.message_handler(state=MyDialog.cylinder_otvet)
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


@dp.message_handler(state=MyDialog.sheet_otvet)
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
            await MyDialog.sheet_otvet.set()
