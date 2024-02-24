# Модуль os предоставляет множество функций для работы с операционной системой.
# Нам тут он нужен для создания папок
import os

# Модуль shutil - это модуль стандартной библиотеки Python,
# который предоставляет набор функций для манипулирования файлами и директориями.
import shutil

# Модуль для работы с датами и временем
import datetime

# указываем путь к родительской директории в которой хранятся заявки
parent_directory = "D:/YandexDisk/Труд/0_В работе/2023"
# parent_directory = "D:/YandexDisk/"

num = int(input("введите номер последней заявки "))
month = input("введите номер текущего месяца ")
now = datetime.datetime.now()
year = str(now.year)
folderNum = int(input("введите количество папок которое надо создать "))


for i in range(folderNum):

    # задаем имя новой папки заявки в формате NNN-MM-YYYY,
    # NNN - номер порядковый в текущем году
    # MM - месяц
    # YYYY - год
    num = num + 1
    zayavka_folder_name = str(num) + "-" + month + "-" + year + "_"

    # создаем новую директорию
    new_directory = os.path.join(parent_directory, zayavka_folder_name)
    os.mkdir(new_directory)

    folder_directory = parent_directory + "/" + zayavka_folder_name
    new_folder_name = "Чеклисты"
    new_directory = os.path.join(folder_directory, new_folder_name)
    os.mkdir(new_directory)

    new_folder_name = "Фото и видео"
    new_directory = os.path.join(folder_directory, new_folder_name)
    os.mkdir(new_directory)

    new_folder_name = "ТЗ"
    new_directory = os.path.join(folder_directory, new_folder_name)
    os.mkdir(new_directory)

    shutil.copy(parent_directory + "/ТЗ.odt",
                parent_directory + "/" + zayavka_folder_name + "/ТЗ/" + zayavka_folder_name + "ТЗ_в1р1.odt")

    new_folder_name = "Счета входящие"
    new_directory = os.path.join(folder_directory, new_folder_name)
    os.mkdir(new_directory)

    new_folder_name = "Схема"
    new_directory = os.path.join(folder_directory, new_folder_name)
    os.mkdir(new_directory)

    new_folder_name = "ПО"
    new_directory = os.path.join(folder_directory, new_folder_name)
    os.mkdir(new_directory)

    new_folder_name = "КП"
    new_directory = os.path.join(folder_directory, new_folder_name)
    os.mkdir(new_directory)
    shutil.copy(parent_directory + "/КП.xls",
                parent_directory + "/" + zayavka_folder_name + "/КП/" + zayavka_folder_name + "_КП_в1р1.xls")

    new_folder_name = "Паспорт"
    new_directory = os.path.join(folder_directory, new_folder_name)
    os.mkdir(new_directory)

    new_folder_name = "Документы"
    new_directory = os.path.join(folder_directory, new_folder_name)
    os.mkdir(new_directory)

input("Папка создана, нажмите enter для выхода")
