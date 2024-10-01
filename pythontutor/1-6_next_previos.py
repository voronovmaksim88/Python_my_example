"""
Задача «Следующее и предыдущее»
Условие
Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере (пробелы важны!).
"""

n = int(input())
next_n = n + 1
previous_n = n - 1
print("The next number for the number " + str(n) + " is " + str(next_n))
print("The previous number for the number " + str(n) + " is " + str(previous_n))
