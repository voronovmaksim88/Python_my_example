"""
Функция all() возвращает значение True, если все элементы в итерируемом объекте - истинны,
в противном случае она возвращает значение False. Если передаваемая последовательность пуста,
то функция all() также возвращает True

Функция any() возвращает True, если какой-либо (любой) элемент в итерируемом объекте является истинным,
в противном случае any() возвращает значение False.
Если последовательность пуста, то функция any() возвращает False.
"""

test_list = [10, 20, 30]
if all([i > 5 for i in test_list]):
    print("all item of test_list > 5 ")

test_list1 = [True, 1, "True", 1.6]
if all(test_list1):
    print("all item of test_list1 is True ")

test_list2 = [True, 0, None, ""]
if any(test_list2):
    print("any item of test_list2 is True ")
