# программа для поиска простых чисел
# берём все числа подряд
# и пытаемся их делить на все числа от 2 до половины исследуемого числа +1
# примитивно, но работает

import time

start_time = time.time()
maximum = 10000
print("число 2 простое")  # первое простое число, его не ищем
for i in range(3, maximum+1):  # диапазон от 3 до maximum с шагом 1 по умолчанию
    for i1 in range(i // 2 + 1, 1, -1):
        # print(i, "%", i1, "=", i % i1, end='   ')
        if i % i1 == 0:
            print("число", i, "не простое")
            break
        if i1 == 2:
            print("число", i, "простое")
    # print( end = '   ')

a = round((time.time() - start_time), 2)
print()
print(a, "секунд")
input("для завершения нажмите enter")
