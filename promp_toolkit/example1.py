from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.shortcuts import CompleteStyle
from prompt_toolkit.patch_stdout import patch_stdout

commands = ['help', 'exit', 'show', 'add', 'delete', 'edit']
command_completer = WordCompleter(commands, ignore_case=True)

def main():
    print("Добро пожаловать в интерактивную командную строку!")
    print("Введите команду (help для списка команд).")

    while True:
        with patch_stdout():  # Используем patch_stdout
            user_input = prompt('> ', completer=command_completer, complete_style=CompleteStyle.MULTI_COLUMN)

        if user_input == 'help':
            print("Доступные команды: help, exit, show, add, delete, edit")
        elif user_input == 'exit':
            print("Выход из программы.")
            break
        elif user_input == 'show':
            print("Показываем что-то...")
        elif user_input == 'add':
            print("Добавляем что-то...")
        elif user_input == 'delete':
            print("Удаляем что-то...")
        elif user_input == 'edit':
            print("Редактируем что-то...")
        else:
            print(f"Неизвестная команда: {user_input}")

if __name__ == "__main__":
    main()