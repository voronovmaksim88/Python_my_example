import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time() - start_time
        print(f'{func.__name__} выполнилась за {end_time} секунд')
        return result

    return wrapper


@timer
def some_function():
    print("hello")


some_function()
