import functools


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Это docstring wrapper'а"""
        return func(*args, **kwargs)

    return wrapper


@my_decorator
def example():
    """Это docstring оригинальной функции"""
    pass


print(example.__name__)  # Выведет "example", а не "wrapper"
print(example.__doc__)  # Выведет docstring оригинальной функции
