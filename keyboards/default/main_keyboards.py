from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

# Клавиатура главного меню
button_weight = KeyboardButton("Расчет масси")
button_geometry = KeyboardButton("Расчет геометрии")
button_bottom = KeyboardButton("Расчет днища")
button_flange = KeyboardButton("Справочник фланцев")
button_weld = KeyboardButton("Таблица снятия усиления")

main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False).row(
    button_weight, button_geometry).row(button_bottom, button_flange).add(button_weld)

# клавиатура расчета масси
button_list = KeyboardButton("Масса листа")
button_krug = KeyboardButton("Масса круга")
button_pronlad = KeyboardButton("Масса прокладки")
button_truba = KeyboardButton("Масса трубы")
button_main_menu = KeyboardButton("Главное меню")


mass_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False).row(
    button_list, button_krug).row(button_pronlad, button_truba).add(button_main_menu)

# клавиатура  расчета геометрии
button_sweep = KeyboardButton("Расчет развертки по средней линни")
button_perimeter = KeyboardButton("Разчет длини развертки по периметру")
button_height = KeyboardButton("Висота цилендрической части")
button_cylindric = KeyboardButton("Объем цилендрической части")
button_tank = KeyboardButton("Объем резервууара")

geom_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False).row(button_sweep, button_perimeter)\
    .add(button_height).row(button_cylindric, button_tank).add(button_main_menu)
