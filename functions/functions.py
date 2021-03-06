import math


def revers(a, b):
    """
    Функция для реверса полученних данных
    Применяестся для реверсного расчета
    :return: возвращает
    """
    a, b = b, a
    return a, b


def input_data(string: str):
    """
    Разбивает строчку полученною от пользователя на елементи по разделителю + и
    возвращает список елементов.
    :param string: строчка принятая от пользователя в формате a+b+c+...+n
    :return:  возвращает список [a,b,c,...,n]
    >>> input_data("100+200+600")
    [100.0, 200.0, 600.0]
    """
    plot_list = list(map(float, string.split("+")))
    return plot_list


# ------------------------------- Блок расчета масси ---------------------------------------------------------------
def weight_sheet(width: float, length: float, thickness: float, number_of_sheets: int = 1, density: int = 7850):
    """
    Функция для  расчета масси листа
    :param width: длина листа в мм
    :param length: ширина листа в мм
    :param thickness: толщина листа в мм
    :param density: плотность материала в кг/м3 по умолчанию сталь =7850кг/м3
    :param number_of_sheets: количество листов в шт по умолчанию =1шт
    :return: масса листа в тонах с округленнием до 3 знаков

    >>> weight_sheet(1000,1000,1000)
    7.85
    >>> weight_sheet(1000,1000,1000,2000,5)
    10.0
    """
    if number_of_sheets == 1:
        weight: float = width / 1000 * length / 1000 * thickness / 1000 * density / 1000 * number_of_sheets
        return "Масса листа {} тонны".format(round(weight, 3))
    else:
        one_weight: float = width / 1000 * length / 1000 * thickness / 1000 * density / 1000
        weight: float = width / 1000 * length / 1000 * thickness / 1000 * density / 1000 * number_of_sheets
        return "Масса одного листа {1} тонны \nМасса {2} листов {0} тонны".format(round(weight, 3),
                                                                                  round(one_weight, 3),
                                                                                  int(number_of_sheets))


def weight_cylinder(diameter: float, length: float, density: int = 7850):
    """
    Функция для расчета маси круга
    :param diameter: диаметр круга в мм
    :param length: длина круга в мм
    :param density: плотность материала в кг/м3 по умолчанию сталь =7850кг/м3
    :return: масса круга в килограмах с округленнием до 3 знаков в кг

    >>> weight_cylinder(1000, 500)
    3082.688
    >>> weight_cylinder(1500, 200, 2000)
    706.858
    """
    weight: float = (math.pi / 4) * (diameter / 1000) ** 2 * density * length / 1000
    return "Масса круга диаметром {1}mm длиной {2}mm состовляет {0} кг".format(round(weight, 3), diameter, length)


def weight_pipe(diameter: float, wall_thickness: float, length: float, density: int = 7850):
    """
    Функция для расчета маси трубы по диаметру и толщине стенки
    :param diameter: наружний диаметр трубы а мм
    :param wall_thickness: толщина сткнки в мм
    :param length: длина трубы в мм
    :param density: плотность материала в кг/м3 по умолчанию сталь =7850кг/м3
    :return: масу трубы, масса 1-го метра трубы в кг
    >>> weight_pipe(1000, 35, 3000)
    (2498.83, 832.94)
    >>> weight_pipe(300, 20, 2500, 8960)
    (394.08, 157.63)
    """
    diameter_small = diameter - wall_thickness * 2
    weight: float = (math.pi / 4) * ((diameter / 1000) ** 2 - (diameter_small / 1000) ** 2) * length / 1000 * density
    weight_one_meter: float = weight / (length / 1000)
    return "Масса трубы {2}x{3} длиной {4} составляет {0} кг\nМасса одного метра составляет {1} кг".format(
        round(weight, 2), round(weight_one_meter, 2), diameter, wall_thickness, length)


def weight_gasket(diameter_outer: float, diameter_inner: float, length: float = 3, density: int = 2000):
    """
    Функция для расчета маси паранитових прокладок по внутренему и внешнему диаметру
    :param diameter_outer: наружный диаметр в мм
    :param diameter_inner: внутрений диаметр в мм
    :param length: толшина прокладки по умолчанию 3мм
    :param density: плотность материала в кг/м3 по умолчанию паранит = 2000 кг/м3
    :return: масу паронитовой прокладки в кг
    >>> weight_gasket(100, 50)
    0.0353
    >>> weight_gasket(1000, 500, 40, 1800)
    42.4115
    """
    weight: float = (math.pi / 4) * (
            (diameter_outer / 1000) ** 2 - (diameter_inner / 1000) ** 2) * length / 1000 * density
    return "Масса прокладки {1}x{2}x{3} состовляет {0} кг".format(round(weight, 4), diameter_outer,
                                                                  diameter_inner, length)


# --------------------------------------------блок расчета геометрии --------------------------------------------------


def cylinder_sweep(diameter_inner: int, wall_thickness: int):
    """
    Функция расчета развертки по средней линни из внутренего диаметра
    :param diameter_inner: внутренний диаметр в мм
    :param wall_thickness: толщина стенки в мм
    :return: развертка по средней линии в мм
     >>> cylinder_sweep(3000, 20)
     9488
     >>> cylinder_sweep(1600, 10)
     5058
    """
    average_diameter = diameter_inner + wall_thickness
    sweep = math.pi * average_diameter
    return "Развертка по средней линни {} мм".format(round(sweep))


def bottom_perimeter_sweep(perimeter: int, wall_thickness: int):
    """
    Функция разчета длини развертки по наружному периметру
    :param perimeter: периметр днища в мм
    :param wall_thickness: толщина стенки в мм
    :return: развертка по средней линии в мм
    >>> bottom_perimeter_sweep(9550, 20)
    9487
    >>> bottom_perimeter_sweep(5089, 10)
    5058
    """
    sweep = perimeter - wall_thickness * math.pi
    return "Длина развертки по наружному периметру {} мм".format(round(sweep))


def height_cylindrical_part(diameter_inner: int, volume: float):
    """
    расчет висоты цилендрической части резервуара по объему и диаметру
    :param diameter_inner: внутренний диаметр в мм
    :param volume: объем цилиндра в м3
    :return: высота целендрической части в мм
    >>> height_cylindrical_part(1000, 10)
    12732
    >>> height_cylindrical_part(3200, 100)
    12434
    """
    height = 4 * volume / (math.pi * (diameter_inner / 1000) ** 2)
    return "Висота цилендрической части резервуара {} mm".format(round(height * 1000))


def volume_cylindrical_part(diameter_inner: int, height: int):
    """
    Расчет объема цилендрической части по диаметру и висотой цилиндра
    :param diameter_inner: внутренний диаметр в мм
    :param height: высота целендрической части в мм
    :return: объем цилиндра в м3
    >>> volume_cylindrical_part(1000, 12732)
    10
    >>> volume_cylindrical_part(3200, 12434)
    100
    """
    volume = (math.pi * (diameter_inner / 1000) ** 2 * height / 1000) / 4
    return "Объем цилендрической части {} м3".format(round(volume, 2))


def tank_volume(diameter_inner: int, height: int, cylinder_height_part: int,
                elliptic_coefficient: float = 0.25):
    """
    Расчет объема резервууара
    :param diameter_inner: внутренний диаметр в мм
    :param height: высота целендрической части в мм
    :param cylinder_height_part: высота целендрической части днища в мм
    :param elliptic_coefficient: коэффициент эллиптичности по умолчанию 0,25, для днищь
    пониженной елептичности 0,2
    :return:объем резервуара в м3

    >>> tank_volume(1000, 1245, 50)
    1.32
    >>> tank_volume(1000, 1245, 50, 0.2)
    1.27
    """
    # TODO: проверить правельность расчетов с помощью 3D моделей
    if elliptic_coefficient == 0.25:
        bottom_volume = math.pi / 4 * (diameter_inner / 1000) ** 2 * (cylinder_height_part / 1000 +
                                                                      0.166 * diameter_inner / 1000)
    elif elliptic_coefficient == 0.2:
        bottom_volume = math.pi / 4 * (diameter_inner / 1000) ** 2 * (cylinder_height_part / 1000 +
                                                                      0.133 * diameter_inner / 1000)
    else:
        return "Неправильный коефециент елептичности"

    volume_cylindrical = (math.pi * (diameter_inner / 1000) ** 2 * height / 1000) / 4

    result = bottom_volume * 2 + volume_cylindrical
    return "Объем резервууара {} м3".format(round(result, 2))


# --------------------------------------------блок расчета днищь --------------------------------------------------


def calculation_bottom(diameter_inner: int, cylinder_height_part: int, wall_thickness: int,
                       elliptic_coefficient: float = 0.25, density: int = 7850):
    """
    Расчет параметров днища:
    f - площадь внутренней поверхности днища в м2
    d - теоретический диаметр заготовки в мм
    q - масса днища в кг
    v - объем днища в м3
    :param diameter_inner: внутренний диаметр в мм
    :param cylinder_height_part: высота целендрической части днища в мм
    :param wall_thickness:  толщина стенки в мм
    :param elliptic_coefficient: коэффициент эллиптичности по умолчанию 0,25, для днищь
    пониженной елептичности 0,2
    :param density: плотность материала в кг/м3 по умолчанию сталь =7850кг/м3
    :return: f, d, q, v
    >>> calculation_bottom(1600,40, 10)
    (2.98, 1958, 236.4, 0.614)
    >>> calculation_bottom(1600, 40, 10, 0.2, 8000)
    (2.76, 1885, 223.4, 0.508)
    """
    if elliptic_coefficient == 0.25:

        f = math.pi * diameter_inner / 1000 * (cylinder_height_part / 1000 + 0.345 * diameter_inner / 1000)

        d = 2 * math.sqrt((diameter_inner + wall_thickness) * (cylinder_height_part + 0.345 * 1
                                                               * (diameter_inner + wall_thickness)))

        q = math.pi * density * wall_thickness / 1000 * (diameter_inner / 1000 + wall_thickness / 1000) \
            * (cylinder_height_part / 1000 + 0.345 * 1 * (diameter_inner / 1000 + wall_thickness / 1000))

        v = math.pi / 4 * (diameter_inner / 1000) ** 2 * (cylinder_height_part / 1000 +
                                                          0.166 * diameter_inner / 1000)
        return "Площадь внутренней поверхности днища {0} м2\n" \
               "Теоретический диаметр заготовки {1} мм\n" \
               "Масса днища {2} кг\n" \
               "Объем днища {3} м3\n" \
               "коэффициент эллиптичности {4}".format(round(f, 2), round(d), round(q, 1), round(v, 3),
                                                      elliptic_coefficient)

    elif elliptic_coefficient == 0.2:
        f = math.pi * diameter_inner / 1000 * (cylinder_height_part / 1000 + 0.318 * diameter_inner / 1000)

        d = 2 * math.sqrt((diameter_inner + wall_thickness) * (cylinder_height_part + 0.318
                                                               * (diameter_inner + wall_thickness)))

        q = math.pi * density * wall_thickness / 1000 * (diameter_inner / 1000 + wall_thickness / 1000) \
            * (cylinder_height_part / 1000 + 0.318 * (diameter_inner / 1000 + wall_thickness / 1000))

        v = math.pi / 4 * (diameter_inner / 1000) ** 2 * (cylinder_height_part / 1000 +
                                                          0.133 * diameter_inner / 1000)

        return "Площадь внутренней поверхности днища {0} м2\n" \
               "Теоретический диаметр заготовки {1} мм\n" \
               "Масса днища {2} кг\n" \
               "Объем днища {3} м3\n" \
               "коэффициент эллиптичности {4}".format(round(f, 2), round(d), round(q, 1), round(v, 3),
                                                      elliptic_coefficient)
    else:
        return "Введен неправельный коефициент елептичности. Поробуйте снова"


# -------------------------------------------блок снятия усиления шва ---------------------------------------


if __name__ == '__main__':
    import doctest

    doctest.testmod()
