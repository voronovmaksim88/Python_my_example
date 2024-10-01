""" РЕШЕНО !!!!
Задача «Родословная: подсчет уровней»
Условие
В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель.
Каждом элементу дерева сопоставляется целое неотрицательное число, называемое высотой.
У родоначальника высота равна 0, у любого другого элемента высота на 1 больше, чем у его родителя.
Вам дано генеалогическое древо, определите высоту всех его элементов.
Программа получает на вход число элементов в генеалогическом древе N.
Далее следует N−1 строка, задающие родителя для каждого элемента древа, кроме родоначальника.
Каждая строка имеет вид имя_потомка имя_родителя.
Программа должна вывести список всех элементов древа в лексикографическом порядке.
После вывода имени каждого элемента необходимо вывести его высоту.
Примечание

Эта задача имеет решение сложности O(n), но вам достаточно написать решение сложности O(n2)
(не считая сложности обращения к элементам словаря).
"""

i = int(input())
rod_dict = dict()  # словарь родителей и потомков
for a in range(0, i - 1):
    pot_rod_str = input()
    pot_rod_list = pot_rod_str.split()
    # print (pot_rod_str)
    # print (pot_rod_list)
    rod_dict[pot_rod_list[0]] = pot_rod_list[1]

#  print(pot_rod_dict)
#  print(pot_rod_dict.keys())
#  print(pot_rod_dict.values())

#  rod_set = set(["123456","7777"])
rod_set = set()

name_set = set(rod_dict.keys()) | set(rod_dict.values())
#  print(type(name_set))
#  print(name_set)

name_list = list(name_set)
#  print(type(name_list))
#  print(name_list)

name_list = sorted(name_list)
#  print(name_list)

for i in name_list:
    print(i, end=" ")
    height = 0
    j = i
    while True:
        if j not in set(rod_dict.keys()):  # если человек не является не чьим потомком, то он верховный родитель
            print(height)
            break
        if j in set(rod_dict.keys()):
            height += 1
            j = rod_dict[j]
            continue
