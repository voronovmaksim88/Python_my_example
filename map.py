# Маппинг — это функция, которая применяет другую функцию к итерируемому объекту.
# map(function, iterable, *iterables)¶
# Return an iterator that applies function to every item of iterable, yielding the results.
# map возвращает итератор

ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def my_fn(x):
    return x * 2


r = map(my_fn, ls)  # Заметили, что скобок у my_func нет?
print(r)
print(type(r))
print(list(r))  # Выводит список, который содержит итератор
