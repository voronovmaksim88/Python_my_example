num = int(input("Введите число от 0 до 4\n"))  # \n  для перевода на новую строку
if num == 0:
    print("Вы ввели 0")
elif num == 1:
    print("Вы ввели 1")
elif num == 2 or num == 3:
    print("Вы ввели 2 или 3")
else:
    print("Вы ввели неподходящее число")
