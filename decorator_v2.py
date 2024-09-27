import time  # Импортируем модуль time для работы со временем


# Определяем декоратор для измерения времени выполнения функции
def timer(func):
    # Определяем обертку для оригинальной функции
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Запоминаем время старта функции
        result = func(*args, **kwargs)  # Вызываем оригинальную функцию и сохраняем результат
        end_time = time.time() - start_time  # Вычисляем время выполнения функции
        # Печатаем имя функции и время ее выполнения.
        print(f'{func.__name__} выполнилась за {end_time} секунд')
        return result  # Возвращаем результат работы оригинальной функции

    return wrapper  # Возвращаем обёртку


# Декорируем функцию sum_function декоратором timer для измерения ее времени выполнения
@timer
def sum_function():
    summ = 0  # Инициализируем переменную для суммы с начальным значением 0
    print("summ from 0 to 10 000 000 is:")  # Печатаем начальное сообщение
    for i in range(0, 10_000_001):  # Проходим циклом по диапазону от 0 до 10 000 000 включительно
        summ += i  # Прибавляем каждое число к сумме
    print(summ)  # Выводим итоговую сумму


sum_function()  # Вызываем декорированную функцию sum_function