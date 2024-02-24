# with as это менеджер контекста.
# Нужна для выполнения важных функций при ошибке
with open('test.txt', 'wt', encoding='utf-8') as inFile:
    num1 = int(input("Введите первое число "))
    num2 = int(input("Введите второе число "))
    line = str(str(num1) + " + " + str(num2) + ' = ' + str(num1 + num2) + "  записано в файл")
    print(line)
    inFile.write(line)
    # при возникновении ошибки файл закроется
