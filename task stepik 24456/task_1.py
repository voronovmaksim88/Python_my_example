"""
Если приведенная ниже задача кажется вам сложной, то вам следует пройти первый курс по языку Python,
который не требует начальных знаний языка: https://stepik.org/course/Программирование-на-Python-67﻿.

Реализуйте программу, которая принимает последовательность чисел и выводит их сумму.

Вашей программе на вход подается последовательность строк.
Первая строка содержит число n (1 ≤ n ≤ 100).
В следующих n строках содержится по одному целому числу.

Выведите одно число – сумму данных n чисел.
"""

num_qty = int(input())
summa = 0
for i in range(num_qty):
    num = int(input())
    summa += num
print(summa)
