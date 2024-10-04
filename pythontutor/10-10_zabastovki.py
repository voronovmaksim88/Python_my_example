"""
Занятие 10. Множества
Задача «Забастовки»
Условие

Политическая жизнь одной страны очень оживленная.
В стране действует K политических партий, каждая из которых регулярно объявляет национальную забастовку.
Дни, когда хотя бы одна из партий объявляет забастовку, при условии, что это не суббота или воскресенье
(когда и так никто не работает), наносят большой ущерб экономике страны.
i-я партия объявляет забастовки строго каждые b_i дней, начиная с дня с номером a_i.
То есть i-я партия объявляет забастовки в дни a_i, a_i + b_i, a_i + 2 * b_i и т.д.
Если в какой-то день несколько партий объявляет забастовку, то это считается одной общенациональной забастовкой.
В календаре страны N дней, пронумерованных, начиная с единицы.
Первый день года является понедельником, шестой и седьмой дни года — выходные, неделя состоит из семи дней.
В первой строке даны числа N и K. Далее идет K строк, описывающие графики проведения забастовок.
i-я строка содержит числа a_i и b_i. Вам нужно определить число забастовок, произошедших в этой стране в течение года.
"""
z = 0  # число забастовок
str_nk = input()
n, k = int(str_nk.split()[0]), int(str_nk.split()[1])
# print(n,k)
days = set()
for i in range(1, n + 1):
    days.add(i)
# print(days)

# удаляем выходные дни
week_num = 0
if n % 7 == 0:
    week_num = n//7
else:
    week_num = n//7 + 1
# print("week_num", week_num)

for i in range(7, week_num * 7+1, 7):
    if i in days:
        days.remove(i)
    if i-1 in days:
        days.remove(i - 1)
# print("не выходные дни", days)
# print("кол-во не выходных дней", len(days))


for i in range(1, k + 1):
    str_ab = input()
    a, b = int(str_ab.split()[0]), int(str_ab.split()[1])
    for j in range(a, n + 1, b):
        # print(j)
        if j in days:
            days.remove(j)
            z = z + 1

print(z)