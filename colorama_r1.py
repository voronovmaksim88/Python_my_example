# pip install colorama
import colorama
from colorama import Fore, Style

# Инициализация colorama для перехвата символов цвета в Windows
colorama.init(autoreset=True)

num = 123  # Задаем числовую переменную

print(Fore.BLUE + str(num))  # Выводим значение переменной голубым цветом
print(Fore.LIGHTBLUE_EX + str(num))  # Выводим значение переменной светлоголубым цветом

print(Fore.GREEN + str(num))  # Выводим значение переменной зелёным цветом
print(Fore.LIGHTGREEN_EX + str(num))  # Выводим значение переменной светлозелёным цветом

print(Fore.RED + str(num))  # Выводим значение переменной красным цветом
print(Fore.LIGHTRED_EX + str(num))  # Выводим значение переменной светлокрасным цветом

print(Fore.MAGENTA + str(num))  # Выводим значение переменной сиреневым цветом
print(Fore.LIGHTMAGENTA_EX + str(num))  # Выводим значение переменной сиреневым цветом

print(Fore.YELLOW + str(num))  # Выводим значение переменной жёлтым цветом
print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + str(num) + " bold")  # Выводим значение переменной светложёлтым цветом

print("white hapy end")
