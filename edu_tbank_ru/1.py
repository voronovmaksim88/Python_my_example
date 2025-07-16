"""
Задача: Найти количество пятизначных нечётных чисел, состоящих из различных цифр,
 в десятичной записи которых нет цифр 2, 4, 7, 9.
"""

qty = 0
all_num=[]
for e in [1, 3, 5]:
    for d in [1, 3, 5, 6, 8, 0]:
        for c in [1, 3, 5, 6, 8, 0]:
            for b in [1, 3, 5, 6, 8, 0]:
                for a in [1, 3, 5, 6, 8]:
                    if (e != d and e != c and e != b and e != a and
                            d != c and d != b and d != a and
                            c != b and c != a and
                            b != a):
                        qty = qty + 1
                        print(a, b, c, d, e)
                        # Добавляем число в список
                        num = int(str(a) + str(b) + str(c) + str(d) + str(e))
                        all_num.append(num)

print('qty', qty)
print()

all_num.sort()
for i in all_num:
    print(i)