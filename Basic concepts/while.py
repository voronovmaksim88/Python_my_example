i = 10
while i > 0:
    print(i, " ", end='')
    i = i - 1

print("")
print("Программа будет просить ввести число до тех пор пока вы не введёте 0 или число меньше ноля")
a = int(input("input num "))
while a != 0:
    if a < 0:
        print('Встретилось отрицательное число', a)
        break
    a = int(input("input num "))
else:
    print('Ни одного отрицательного числа не встретилось')

