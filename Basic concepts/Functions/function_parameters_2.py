# Параметр функции может быть списком, для того чтоб функция могла принять неограниченное число аргументов
def print_ab(a, b, *args):
    # args - это кортеж
    print("positional argument a:", a)
    print("positional argument b:", b)
    if args:
        print("additional arguments args:")
        for arg in args:
            print(arg)
    print()


print_ab(10, 20, 1, 2, 3)
print_ab(a=10, b=20)


