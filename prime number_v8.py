"""
Программа для поиска простых чисел
Простое число - это натуральное число больше 1, единственными делителями которого являются только оно само и единица.
Все остальные натуральные числа называются составными. Натуральное число 1 не является ни простым, ни составным.

Чтобы понять, как работает программа, надо написать на листочке числа в диапазоне например от 0 до 30 и
вычёркивать не простые согласно формуле в цикле. По моему это называется "метод решета"
"""

import time

start_time = time.time()
i = 200_000_000
print("начинаем поиск простых чисел с ", i)
stop = ''
while True:
    i = i + 1
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            # print(i, "не простое")
            break
        if j == i // 2:
            print(i, end=" ")
            b = round((time.time() - start_time), 1)
            print(b, "сек")
            start_time = time.time()
            stop = input("Введите Y  для завершения ")
    #  print(i)
# print("На поиск затрачено", b, "секунд")