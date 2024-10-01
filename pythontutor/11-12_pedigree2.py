""" РЕШЕНО !!!!
Условие
Даны два элемента в дереве. Определите, является ли один из них потомком другого.
Во входных данных записано дерево в том же формате, что и в предыдущей задаче Далее идет число запросов K.
В каждой из следующих K строк, содержатся имена двух элементов дерева.
Для каждого такого запроса выведите одно из трех чисел:
1, если первый элемент является предком второго,
2, если второй является предком первого или
0, если ни один из них не является предком другого.
"""

"""
9
Alexei Peter_I
Anna Peter_I
Elizabeth Peter_I
Peter_II Alexei
Peter_III Anna
Paul_I Peter_III
Alexander_I Paul_I
Nicholaus_I Paul_I
5
Anna Nicholaus_I
Peter_II Peter_I
Alexei Paul_I
Alexei Peter_I
Nicholaus_I Peter_I
"""

"""
                    Peter_I
    Alexei          Anna                 Elizabeth
   Peter_II       Peter_III
                   Paul_I
           Alexander_I   Nicholaus_I
"""

N = int(input())  # принимаем количество строк "потомок родитель"
pot_rod_dict = dict()  # создаём словарь в котором ключи-потомки родители-значения
for a in range(0, N - 1):
    pot_rod_str = input()  # считываем строку "потомок родитель"
    pot_rod_list = pot_rod_str.split()  # делим строку на два значения, кладём их в список
    pot_rod_dict[pot_rod_list[0]] = pot_rod_list[1]  # производим запись в словарь
"""
print()
print(len(pot_rod_test_dict))
print(pot_rod_dict)  # выводим весь словарь
print(list(pot_rod_dict.keys()))  # выводим только потомков
print(list(pot_rod_dict.values()))  # выводим только родителей
"""

k = int(input())  # принимаем количество строк "потомок родитель" которые надо проверить на родство
human1_test = list()
human2_test = list()
for a in range(0, k):
    pot_rod_str = input()  # считываем строку "потомок родитель"
    pot_rod_list = pot_rod_str.split()  # делим строку на два значения, кладём их в список
    human1_test.append(pot_rod_list[0])  # производим запись в список первых людей в паре
    human2_test.append(pot_rod_list[1])  # производим запись в список вторых людей в паре


"""
print()
print(len(pot_rod_test_dict))
print(pot_rod_test_dict)  # выводим весь словарь
print(list(pot_rod_test_dict.keys()))  # выводим только потомков
print(list(pot_rod_test_dict.values()))  # выводим только родителей
"""

for i in range(0, len(human1_test)):
    # print(human1_test[i], human2_test[i], end=" ")  # выводим кого тестируем на родство

    j = human1_test[i]
    kinship = -1  # степень родства
    while True:
        if j not in (list(pot_rod_dict.keys())):  # если нет среди потомков значит дошли до верховного родителя
            #  print(123)
            break

        if j in (list(pot_rod_dict.keys())):  # первый тестируемый в паре есть среди потомков
            if pot_rod_dict[j] == human2_test[i]:
                kinship = 2
                print(kinship, end=" ")
                break
            else:
                j = pot_rod_dict[j]
                continue

    j = human2_test[i]
    while True:
        if j not in (list(pot_rod_dict.keys())):  # если нет среди потомков значит дошли до верховного родителя
            #  print(123)
            break

        if j in (list(pot_rod_dict.keys())):  # второй тестируемый в паре есть среди потомков
            if pot_rod_dict[j] == human1_test[i]:
                kinship = 1
                print(kinship, end=" ")
                break
            else:
                j = pot_rod_dict[j]
                continue
    if kinship == -1:
        print(0, end=" ")
