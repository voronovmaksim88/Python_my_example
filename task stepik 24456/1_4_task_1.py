"""
Реализуйте программу, которая будет эмулировать работу с пространствами имен. Необходимо реализовать поддержку создания
 пространств имен и добавление в них переменных.

В данной задаче у каждого пространства имен есть уникальный текстовый идентификатор – его имя.

Вашей программе на вход подаются следующие запросы:

create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
add <namespace> <var> – добавить в пространство <namespace> переменную <var>
get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе из пространства
 <namespace>, или None, если такого пространства не существует
Рассмотрим набор запросов

add global a
create foo global
add foo b
create bar foo
add bar a
Структура пространств имен описанная данными запросами будет эквивалентна структуре пространств имен,
 созданной при выполнении данного кода

a = 0
def foo():
  b = 1
  def bar():
    a = 2
В основном теле программы мы объявляем переменную a, тем самым добавляя ее в пространство global.
 Далее мы объявляем функцию foo,
  что влечет за собой создание локального для нее пространства имен внутри пространства global.
  В нашем случае, это описывается командой create foo global. Далее мы объявляем внутри функции foo функцию bar,
   тем самым создавая пространство bar внутри пространства foo, и добавляем в bar переменную a.

Добавим запросы get к нашим запросам

get foo a
get foo c
get bar a
get bar b
Представим как это могло бы выглядеть в коде

a = 0
def foo():
  b = 1
  get(a)
  get(c)
  def bar():
    a = 2
    get(a)
    get(b)
Результатом запроса get будет имя пространства, из которого будет взята нужная переменная.
Например, результатом запроса get foo a будет global, потому что в пространстве foo не объявлена переменная a,
 но в пространстве global, внутри которого находится пространство foo, она объявлена. Аналогично,
  результатом запроса get bar b будет являться foo, а результатом работы get bar a будет являться bar.

Результатом get foo c будет являться None, потому что ни в пространстве foo,
 ни в его внешнем пространстве global не была объявлена переменная с.

Более формально, результатом работы get <namespace> <var> является

<namespace>, если в пространстве <namespace> была объявлена переменная <var>
get <parent> <var> – результат запроса к пространству, внутри которого было создано пространство <namespace>,
 если переменная не была объявлена
None, если не существует <parent>, т. е. <namespace> – это global
Формат входных данных
В первой строке дано число n (1 ≤ n ≤ 100) – число запросов.
В каждой из следующих n строк дано по одному запросу.
Запросы выполняются в порядке, в котором они даны во входных данных.
Имена пространства имен и имена переменных представляют из себя строки длины не более 10,
 состоящие из строчных латинских букв.

Формат выходных данных
Для каждого запроса get выведите в отдельной строке его результат.



Sample Input:

9
add global a
create foo global
add foo b
get foo a
get foo c
create bar foo
add bar a
get bar a
get bar b
Sample Output:

global
None
bar
foo
"""


# организуем словарь для хранения пространств имен
# ключ - это имя пространства имён
# значение - это список всех переменных, объявленных в данном пространстве имен

def create(data, new_name_spase, parent_name_space):
    """
    Функция принимает на вход наш словарь и команду
    Далее она находит то пространство имён(ключ) в которое надо добавить новое пространство имён
    и добавляет
    """

    if isinstance(data, dict):  # Если текущий элемент - словарь
        for key, value in data.items():
            print(key)  # Выводим ключ
            if key == parent_name_space:
                data[key].append({new_name_spase: []})
            create(value, new_name_spase, parent_name_space)  # Рекурсивный вызов для значения
    elif isinstance(data, list):  # Если текущий элемент - список
        for item in data:
            create(item, new_name_spase, parent_name_space)  # Рекурсивный вызов для каждого элемента списка


def add(data, name_spase, var):
    """
    Функция принимает на вход наш словарь, имя пространства имён и и имя переменной
    """

    if isinstance(data, dict):  # Если текущий элемент - словарь
        for key, value in data.items():
            # print(key)  # Выводим ключ
            if key == name_spase:
                data[key].append(var)
            add(value, name_spase, var)  # Рекурсивный вызов для значения
    elif isinstance(data, list):  # Если текущий элемент - список
        for item in data:
            add(item, name_spase, var)  # Рекурсивный вызов для каждого элемента списка


def get(data, name_spase, var):
    """
        Функция принимает на вход наш словарь, имя пространства имён и имя переменной.
        Для переменной надо вернуть имя того пространства имён из которого она будет взята
        или вернуть None если такого пространства не существует
    """

    if isinstance(data, dict):  # Если текущий элемент - словарь
        for key, value in data.items():
            name_spase = key
            return get(value, name_spase, var)  # Рекурсивный вызов для значения

    elif isinstance(data, list):  # Если текущий элемент - список
        for i in range(len(data)):
            if data[i] == var:
                return "variable " + data[i] + " was found in namespace " + name_spase
            if isinstance(data[i], dict):
                return get(data[i], name_spase, var)  # Рекурсивный вызов для каждого элемента списка
            if i == len(data) - 1:
                return None

    # elif isinstance(data, str):  # Если текущий элемент - список
    #     if data == var:
    #         return "variable " + data + " was found in namespace " + name_spase
    #     else:
    #         return None


# словарь для хранения пространств имен
# name_space_dict = {'global': [{'foo': [{'f2': []}, {'f3': []}]}, {'foo1': []}]}
name_space_dict = {'global': []}

add(name_space_dict, 'global', 'v_01')
add(name_space_dict, 'global', 'v_02')
add(name_space_dict, 'global', 'v_03')

create(name_space_dict, 'ns1', 'global')
add(name_space_dict, 'global', 'v_04')
add(name_space_dict, 'ns1', 'v_10')
add(name_space_dict, 'ns1', 'v_11')

create(name_space_dict, 'ns2', 'ns1')
add(name_space_dict, 'ns2', 'v_20')
add(name_space_dict, 'ns2', 'v_21')

print(get(name_space_dict, 'ns1', 'v_12'))
print()

print(name_space_dict)


# request_qty = int(input())
# for i in range(request_qty):
#     command, arg1, arg2 = input().split()
#     if command == "add":
#         # arg1 - это имя пространства имён
#         name_space_dict[arg1].append(arg2)
#
#     if command == "create":
#         # arg1 - Это имя пространства имён, которое надо создать.
#         # arg2 - Это имя пространства, внутри которого надо создать.
#         for name_space in name_space_dict:
#             if name_space == arg2:
#                 name_space_dict[name_space].append({arg1: []})
#
#     if command == "get":
#         print(name_space_dict[arg2])
#
# print(name_space_dict)

# def print_keys(data):
#     if isinstance(data, dict):  # Если текущий элемент - словарь
#         for key, value in data.items():
#             print(key)  # Выводим ключ
#             print_keys(value)  # Рекурсивный вызов для значения
#     elif isinstance(data, list):  # Если текущий элемент - список
#         for item in data:
#             print_keys(item)  # Рекурсивный вызов для каждого элемента списка
#
# # Пример использования
# example = {"G": [{"f": [{"f1": []}]}]}
# print_keys(example)


def print_name_space(name_space_dict_in: dict, tab="", i=0):
    name = list(name_space_dict_in.keys())[0]
    for item in name_space_dict_in[name]:
        if type(item) is str:
            print(f"{tab} {item} = {i}")
            i += 1
    for item in name_space_dict_in[name]:
        if type(item) is dict:
            print(f"{tab}def {list(item.keys())[0]}():")
            print_name_space(item, tab + "  ", i)


print_name_space(name_space_dict)
