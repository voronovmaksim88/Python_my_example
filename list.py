my_list = []
print(my_list)

numbers = list()
numbers = [1, 2, 3, 4, 5]
print(numbers)

my_list.append(1)
print(my_list)

my_list.append(2)
print(my_list)

for i in range(0, len(my_list)):
    my_list[i] = str(my_list[i])
print(my_list)

# Допустим, у нас есть список:
my_list = [1, 2, 3, 2, 4, 2, 5]

# Мы хотим посчитать количество вхождений числа 2:
count = my_list.count(2)

print(count)  # Выведет 3, потому что число 2 встречается в списке 3 раза.
