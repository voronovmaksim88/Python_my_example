# Параметры функции могут быть именованными и не именованными

def print_ab(a, b):
    print(a, b)


def print_ab1(a, b=0):
    print(a, b)


def print_ab2(a=0, b=0):
    print(a, b)

# так нельзя делать
# def print_ab3(a=0, b):
#     print(a, b)
