from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button_weight = KeyboardButton("Расчет масси")
button_geometry = KeyboardButton("Расчет геометрии")
button_bottom = KeyboardButton("Расчет днища")

main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    button_bottom, button_geometry, button_weight
)


button_list = KeyboardButton("Масса листа")
button_krug = KeyboardButton("Масса круга")
button_pronlad = KeyboardButton("Масса прокладки")
button_truba = KeyboardButton("Масса трубы")


mass_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    button_list, button_krug, button_pronlad, button_truba
)

button_sweep = KeyboardButton("расчета развертки по средней линни")
button_perimeter = KeyboardButton("разчета длини развертки")
button_height = KeyboardButton("висоты цилендрической части")
button_cylindric = KeyboardButton("объема цилендрической части")
button_tank = KeyboardButton("Расчет объема резервууара")

geom_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    button_sweep, button_perimeter, button_height, button_cylindric, button_tank
)
