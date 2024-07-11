# pip install colorama
import colorama
from colorama import Fore, Style

# Инициализация colorama для перехвата символов цвета в Windows
colorama.init(autoreset=True)

num = 123  # Задаем числовую переменную

print(Fore.BLUE + str(num))  # Выводим значение переменной голубым цветом
print(Fore.LIGHTBLUE_EX + str(num))  # Выводим значение переменной светло-голубым цветом

print(Fore.GREEN + str(num))  # Выводим значение переменной зелёным цветом
print(Fore.LIGHTGREEN_EX + str(num))  # Выводим значение переменной светло-зелёным цветом

print(Fore.RED + str(num))  # Выводим значение переменной красным цветом
print(Fore.LIGHTRED_EX + str(num))  # Выводим значение переменной светло-красным цветом

print(Fore.MAGENTA + str(num))  # Выводим значение переменной сиреневым цветом
print(Fore.LIGHTMAGENTA_EX + str(num))  # Выводим значение переменной сиреневым цветом

print(Fore.YELLOW + str(num))  # Выводим значение переменной жёлтым цветом
print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + str(num) + " bold")  # Выводим значение переменной светло-жёлтым цветом

print("white hapy end")
