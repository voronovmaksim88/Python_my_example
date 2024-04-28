# примеры функций

def func_summarize(x, y):
    #  func_summarize - имя функции
    #  x, y - параметры функции
    # от двоеточия до return - тело функции
    summa = x + y
    print(f"{x}+{y}={summa}")
    return summa  # функция возвращает сумму аргументов


def func_print_xy(x, y):
    print(x, y)
    pass  # функция НЕ возвращает Ничего


def func_tuple(*args):  # функция принимает сколько угодно аргументов в виде кортежа
    print(args)
    pass


def func_dictionary(**args):  # функция принимает сколько угодно аргументов в виде словаря
    print(args)
    pass


func_summarize(1, 2)
func_print_xy(1, 2)
func_tuple(1, 2, 3, "abc")
func_dictionary(name="Ivan", age="123")

var_sum = func_summarize  # назначаем переменной функцию
var_sum(3, 4)

# присваиваем переменной результат выполнения функции
var_sum2 = func_summarize(10, 20)
print(var_sum2)
