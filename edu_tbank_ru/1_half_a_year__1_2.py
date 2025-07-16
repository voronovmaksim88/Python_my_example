"""
Про умножение на 2 или перестановку цифр
Гриша научился в школе выполнять с числами только следующие операции: умножать на 2 и произвольным образом
переставлять цифры (нельзя только ставить 0 на первое место).
Выберите все числа, из которых Гриша сможет получить число 86.
Выберите все верные варианты ответа.
7, 13, 17, 23, 43
"""


def test_func(test_num: int):
    test_num=test_num * 2
    print(test_num)

    if test_num > 86:
        return False
    elif test_num == 86:
        return True
    else:
        test_func(test_num)


try:
    num = int(input("Введите число: "))
except ValueError:
    print("Ошибка: Введено не числовое значение")
else:
    print(test_func(num))




