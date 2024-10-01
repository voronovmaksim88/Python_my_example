def list_sum(lst):
    result = 0
    for element in lst:
        result += element
    return result


def summa (a, b):
    return a + b


y = summa(1, 2)
z = list_sum([1, 2, 3])
print(y)
print(z)
