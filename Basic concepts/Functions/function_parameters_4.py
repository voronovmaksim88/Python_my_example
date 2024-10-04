# Параметры функции на максималках
def print_ab(pos_arg1, pos_arg2, pos_arg3,
             pos_arg_with_default_1=1, pos_arg_with_default_2=2,
             *pos_arg_name,
             **kwargs):
    # kwargs - это словарь
    print("pos_arg1:", pos_arg1)
    print("pos_arg2:", pos_arg2)
    print("pos_arg3:", pos_arg3)
    print("pos_arg_with_default_1:", pos_arg_with_default_1)
    print("pos_arg_with_default_2:", pos_arg_with_default_2)
    if pos_arg_name:
        for name in pos_arg_name:
            print(name)

    if kwargs:
        print("additional arguments args:")
        for key in kwargs:
            print(key, kwargs[key])
    print()


print_ab(10, 20, 30, 50, b=20, c=30)
