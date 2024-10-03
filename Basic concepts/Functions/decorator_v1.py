def my_decorator(function_to_decorate):
    # Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой, функции
    # получая возможность исполнять произвольный код до и после неё.
    def wrapper():
        print("Я - код, который отработает до вызова функции")
        function_to_decorate()  # Сама функция
        print("А я - код, срабатывающий после")

    return wrapper


@my_decorator
def stand_alone_function():
    print("  Я простая одинокая функция ?")


stand_alone_function()
