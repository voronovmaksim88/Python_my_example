my_test_list = [1, 2, 1.2, "a", "abc", ["x", "y"], {'a': 1}, True]  # объявляем список
print('my_test_list =', my_test_list)  # выводим его в консоль

my_test_list = list("string")
print('list("string") =', my_test_list)

my_test_list = list({'a': 1, 'b': 2})  # список из ключей словаря
print("list({'a': 1, 'b': 2}) =", my_test_list)

my_test_list = list({'a': 1, 'b': 2}.values())  # список из значений словаря
print("list({'a': 1, 'b': 2}.values()) =", my_test_list)
