def print_ab(a, b):
    print(a, " ", b)


print_ab(1, 2)  # Вызов функции с позиционными аргументами

print_ab(b=3, a=4)  # Вызов функции с именованными аргументами

lust_ab = [1, 2]
print_ab(*lust_ab)  # = print_ab(list_ab[0], list_ab[1])

dict_ab = {'a': 1, 'b': 2}
print_ab(**dict_ab)  # = print_ab(dict_ab['a'], dict_ab['b'])
