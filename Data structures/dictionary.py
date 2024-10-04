# Пример создания словаря

"""
Словари в Python — это неупорядоченные коллекции произвольных объектов,
имеющих доступ к ним по ключу.
Словари в основном используются, когда необходимо создать гибкую структуру данных,
обеспечивающую возможность быстрого поиска.
Словарь состоит из пар ключ значение
Одному ключу соответствует только одно значение
Если добавить пару в которой существующий ключ то пара перезапишется, старая сотрётся
"""

dict_contact = {"name": "maksim", "age": 33, "phone": 89138995941}

print(dict_contact)  # вывод словаря
print(dict_contact.keys())  # вывод ключей словаря
print(dict_contact.values())  # вывод значений объектов

if "name" in dict_contact:  # таким образом проверяется есть ли "name" среди ключей словаря
    print("name in dict_contact")

# проверяем наличие в значениях словаря
if "maksim" in dict_contact:  # а вот значение таким образом не найдётся
    print("maksim in dict_contact as key")

if "maksim" in dict_contact.values():  # а вот таким найдётся
    print("maksim in dict_contact as values")

# обновление значения словаря, можно сразу несколько обновить и/или добавить
dict_contact.update({"name": "Ivan"})
dict_contact["age"] = 44  # то же обновление значения словаря
print(dict_contact)  # вывод словаря