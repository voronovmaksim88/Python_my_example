name = input("Как Вас зовут? ")
print("Привет,", name)
print("\u001b[31m Красный текст \u001b[0m")
# \u001b[31m установить красный цвет
# \u001b[0m вернуть белый цвет

print("\u001b[32m Зелёный текст \u001b[0m")
print("\u001b[33m Жёлтый текст \u001b[0m")
print("\u001b[34m Синий текст\u001b[0m")
print("\u001b[35m Пурпурный текст\u001b[0m")
print("\u001b[36m Голубой текст\u001b[0m")
print("\u001b[37m Серый текст\033[0m")

test = 123.2
print(test)

# сложение строк
num1 = input("enter first num ")
num2 = input("enter second num ")
res = num1 + num2
print("result is", res)

# сложение чисел
num1 = int(input("enter first num "))
num2 = int(input("enter second num "))
res = num1 + num2
print("num1+num2 = ", res)
input("press enter for exit")
