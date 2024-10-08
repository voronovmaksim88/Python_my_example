# Учимся работать с кортежем (tuple)
"""
Кортеж в Python — это более быстрый и неизменяемый аналог списка.
Он очень часто используется для защиты хранимых данных приложения от незапланированных или непреднамеренных изменений.
Кортеж также требует выделения значительно меньшего количества памяти.
"""
a = (1, 2, 3, 4, 5, 6, 7, 8, 9)  # это кортеж - неизменяемый список
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # это список

print("size of tuple is ", a.__sizeof__(), "bytes")
print("size of list is ", b.__sizeof__(), "bytes")
