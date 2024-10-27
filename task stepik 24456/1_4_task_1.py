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
            # print(key)  # Выводим ключ
            if key == parent_name_space:
                data[key].append({new_name_spase: []})
            create(value, new_name_spase, parent_name_space)  # Рекурсивный вызов для значения
    elif isinstance(data, list):  # Если текущий элемент - список
        for item in data:
            create(item, new_name_spase, parent_name_space)  # Рекурсивный вызов для каждого элемента списка


def add(data, name_spase, var):
    """
    Функция принимает на вход наш словарь, имя пространства имён и имя переменной
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



# словарь для хранения пространств имен
# name_space_dict = {'global': [{'foo': [{'f2': []}, {'f3': []}]}, {'foo1': []}]}
name_space_dict = {'global': []}
#
# add(name_space_dict, 'global', 'v_01')
# add(name_space_dict, 'global', 'v_02')
# add(name_space_dict, 'global', 'v_03')
#
# create(name_space_dict, 'ns1', 'global')
# add(name_space_dict, 'global', 'v_04')
# add(name_space_dict, 'ns1', 'v_10')
# add(name_space_dict, 'ns1', 'v_11')
#
# create(name_space_dict, 'ns2', 'ns1')
# add(name_space_dict, 'ns2', 'v_20')
# add(name_space_dict, 'ns2', 'v_21')
#
# create(name_space_dict, 'ns3', 'ns2')
#
# print(name_space_dict)
# print()




def print_name_space(name_space_dict_in: dict, tab="", i=0):
    name = list(name_space_dict_in.keys())[0]
    for item in name_space_dict_in[name]:
        if type(item) is str:
            print(f"{tab}{item} = {i}")
            i += 1
    for item in name_space_dict_in[name]:
        if type(item) is dict:
            print(f"{tab}def {list(item.keys())[0]}():")
            print_name_space(item, tab + "  ", i)



def search_in_name_space(data: dict, namespace: str, variable: str) -> bool:
    def find_namespace(current_data):
        # Если текущий элемент словарь
        if isinstance(current_data, dict):
            # Перебираем ключи и значения словаря
            for key, value in current_data.items():
                # Если нашли искомое пространство имен
                if key == namespace:
                    # Проверяем, есть ли переменная в этом пространстве
                    if isinstance(value, list):
                        return variable in value
                    return False
                # Рекурсивно ищем в значении словаря
                result = find_namespace(value)
                if result is not None:  # Если нашли результат (True или False)
                    return result

        # Если текущий элемент список
        elif isinstance(current_data, list):
            # Перебираем элементы списка
            for item in current_data:
                # Если элемент - словарь, ищем в нем
                if isinstance(item, dict):
                    result = find_namespace(item)
                    if result is not None:  # Если нашли результат
                        return result

        return None

    # Специальная обработка для корневого пространства 'global'
    if namespace == 'global':
        if isinstance(data.get('global'), list):
            return variable in data['global']
        return False

    result = find_namespace(data)
    return result if result is not None else False


def create_pass_name_space(data: dict, ns: str) -> list:
    def find_path(current_data, current_path):
        # Если текущий элемент словарь
        if isinstance(current_data, dict):
            # Перебираем ключи и значения словаря
            for key, value in current_data.items():
                # Если нашли искомое пространство имен
                if key == ns:
                    return current_path + [key]
                # Рекурсивно ищем в значении словаря
                path = find_path(value, current_path + [key])
                if path:
                    return path

        # Если текущий элемент список
        elif isinstance(current_data, list):
            # Перебираем элементы списка
            for item in current_data:
                # Рекурсивно ищем в каждом элементе
                path = find_path(item, current_path)
                if path:
                    return path

        return None

    # Начинаем поиск с корневого словаря
    result = find_path(data, [])
    return result if result else []


def get(data: dict,
        name_space_fix: str,
        var_name: str) -> str:
    path = create_pass_name_space(data, name_space_fix)
    path.reverse()
    for ns_i in path:
        in_ns_i = search_in_name_space(name_space_dict, ns_i, var_name)
        if in_ns_i:
            return ns_i
    return "None"


request_qty = int(input())
commands = []
for i in range(request_qty):
    commands.append(input())

# print(commands)

for com in commands:
    command, arg1, arg2 = com.split()
    if command == "add":
        # arg1 - это имя пространства имён
        # name_space_dict[arg1].append(arg2)
        add(name_space_dict, name_spase=arg1, var=arg2)

    if command == "create":
        # arg1 - Это имя пространства имён, которое надо создать.
        # arg2 - Это имя пространства, внутри которого надо создать.
        # for name_space in name_space_dict:
        #     if name_space == arg2:
        #         name_space_dict[name_space].append({arg1: []})
        create(name_space_dict, new_name_spase=arg1, parent_name_space=arg2)

    if command == "get":
        # print(name_space_dict[arg2])
        # arg1 -  <namespace>
        # arg2 -  <var>
        print(get(name_space_dict, name_space_fix=arg1, var_name=arg2))

# print(name_space_dict)

# print()
# print_name_space(name_space_dict)
# print(search_in_name_space(name_space_dict, "global", "v_04"))
# print('путь', create_pass_name_space(name_space_dict, "ns1"))
# print("get result:", get(name_space_dict, 'ns1', 'v_04'))
# print()

