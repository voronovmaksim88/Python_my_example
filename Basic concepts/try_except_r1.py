# изучаем Конструкцию try - except)

# ошибка с делением на ноль
# print (10 / 0)

print("сейчас будем делить число х на число y ")

x_ok = False
y_ok = False
x = 0
y = 0

while not x_ok:
    print("введите число х")
    try:
        x = int(input())
    except ValueError:
        print("вы олень ?")
        x = 0
    else:
        print("отлично !")
        x_ok = True
    finally:  # этот код выполнится в любом случае
        print("поехали дальше !")

while not y_ok:
    print("введите число y")
    try:
        y = int(input())
    except ValueError:
        print("неверный ввод числа")
        y = 0
    else:
        print("отлично !")
        y_ok = True

try:
    res = x / y
except ZeroDivisionError:
    print("на ноль делить нельзя")
    res = 0

if y != 0:
    print("x/y=", res)
