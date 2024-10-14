# программа диалога с пользователем
from datetime import datetime

# Узнаем текущую дату
now = datetime.now()

answer = ""
while answer != "0":
    print("что будем делать ?")
    print("0 выход")
    print("1 вывести год")
    print("2 вывести месяц")
    print("3 вывести число")
    answer = input()
    if answer == "0":
        print("выходим")
    elif answer == "1":
        print("Текущий год:", now.year)
    elif answer == "2":
        print("Текущий месяц:", now.month)
    elif answer == "3":
        print("Текущее число:", now.day)
    else:
        print("не понял ответ")
    print("")
