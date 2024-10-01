""" РЕШЕНО !!!!
Условие
В генеалогическом древе определите для двух элементов их наименьшего общего предка (Lowest Common Ancestor).
Наименьшим общим предком элементов A и B является такой элемент C, что С является предком A, C является предком B,
при этом глубина C является наибольшей из возможных. При этом элемент считается своим собственным предком.
Формат входных данных аналогичен предыдущей задаче
Для каждого запроса выведите наименьшего общего предка данных элементов.
"""

"""
10
Alexei Peter_I
Anna Peter_I
Elizabeth Peter_I
Peter_II Alexei
Peter_III Anna
Paul_I Peter_III
Alexander_I Paul_I
Nicholaus_I Paul_I
Igor Olga
4
Alexander_I Nicholaus_I
Igor Peter_I
Peter_II Paul_I
Alexander_I Anna
"""

"""
                    Peter_I
    Alexei          Anna                 Elizabeth
   Peter_II       Peter_III
                   Paul_I
           Alexander_I   Nicholaus_I
"""

"""
10
ABV UNO
ALO VYN
DBP IDZ
HHY NQX
IDZ ABV
NQX VYN
SXI HHY
UNO ALO
UYP NQX
2
ABV ABV
ABV ALO
"""

"""
     VYN
ALO      NQX                                                            
UNO   UYP   HHY                                                                             
ABV         SXI                                                         
IDZ                                                                
DBP

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


def is_ancestor(man, older_man):
    if man == older_man:
        return True
    while man in pot_rod_dict:
        man = pot_rod_dict[man]
        if man == older_man:
            return True
    return False


for i in range(0, len(human1_test)):
    if is_ancestor(human1_test[i], human2_test[i]):
        print(human2_test[i])
        continue
    if is_ancestor(human2_test[i], human1_test[i]):
        print(human1_test[i])
        continue
    if not is_ancestor(human1_test[i], human2_test[i]) and not is_ancestor(human2_test[i], human1_test[i]):
        if human1_test[i] in pot_rod_dict:
            y = pot_rod_dict[human1_test[i]]
        else:
            y = pot_rod_dict[human2_test[i]]

        while True:
            if is_ancestor(human1_test[i], y) and is_ancestor(human2_test[i], y):
                print(y)
                break
            else:
                if y in pot_rod_dict.keys():
                    y = pot_rod_dict[y]
                    continue
                else:
                    print("")
                    break
