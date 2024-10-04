# Параметр функции может быть словарём
def print_ab(a, b, **kwargs):
    # kwargs - это словарь
    print("positional argument a:", a)
    print("positional argument b:", b)
    if kwargs:
        print("additional arguments args:")
        for key in kwargs:
            print(key, kwargs[key])
    print()


print_ab(a=10, b=20, c=30, d=40)
print_ab(a=10, c=30, d=40, b=20)  # так тоже можно


