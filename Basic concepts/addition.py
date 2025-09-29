
# сложение строк
num1 = input("enter first str ")
num2 = input("enter second str ")
res = num1 + num2
print("num1+num2 = ", res, "\n")

# сложение чисел целых
num1 = int(input("enter first int num "))
num2 = int(input("enter second int num "))
res = num1 + num2
print("num1+num2 = ", res, "\n")

# сложение чисел дробных
num1 = float(input("enter first float num "))
num2 = float(input("enter second float num "))
res = num1 + num2
print("num1+num2 = ", res, "\n")

# сложение логических переменных
num1 = bool(int(input("погода хорошая ? 1-да. 0-нет ")))
num2 = bool(int(input("свободное время  есть ? 1-да 0-нет")))
res = num1 and num2
print("Идём гулять ? ", res, "\n")
input("для завершения нажмите enter")
