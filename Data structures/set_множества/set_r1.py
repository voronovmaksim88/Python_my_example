# главное отличие множества от списка в том, что в множестве нет повторяющихся элементов

def about(x, name):
    print("type", name, "is", type(x))
    print(name, "=", x)
    print()
    # это функция, которая выведет множество


# учимся работать со множествами
# Множество это список в котором элементы не повторяются
my_set_1 = set()  # создали пустое множество
about(my_set_1, "my_set_1")

my_set_2 = {1, "a"}
about(my_set_2, "my_set_2")
# создали непустое множество

my_set_hello = {'h', 'e', 'l', 'l', 'o'}  # создали множество,
# элемент 'l' останется только один поскольку каждый элемент множества уникален
print("my_set_hello=", my_set_hello)

my_set_hello.add('t')  # добавляем новый элемент в множество
print("add t in my_set_hello=", my_set_hello)

my_set_hello.remove('o')  # удаляем элемент из множества
print("del o in my_set_hello=", my_set_hello)
