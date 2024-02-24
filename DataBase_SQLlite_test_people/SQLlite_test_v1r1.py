import sqlite3

con = sqlite3.connect("People_BD.db")
cursor = con.cursor()


create_new_table = 0  # создать таблицу в БД
if create_new_table == 1:
    # создаем таблицу people
    cursor.execute("""CREATE TABLE people
        (id INTEGER PRIMARY KEY AUTOINCREMENT,  
        name TEXT, 
        age INTEGER
        gender INTEGER)
    """)


# добавляем строки в таблицу people
create_new_data = 0  # заполнить таблицу данными
if create_new_data:
    cursor.execute("INSERT INTO people (name, age) VALUES ('Tom', 38)")
    cursor.execute("INSERT INTO people (name, age) VALUES ('Max', 35)")
    cursor.execute("INSERT INTO people (name, age) VALUES ('Den', 35)")
    cursor.execute("INSERT INTO people (name, age) VALUES ('Miron', 9)")
    cursor.execute("INSERT INTO people (name, age) VALUES ('Anastasiya', 35)")


update_data = 1  # изменить данные в таблице
if update_data:
    cursor.execute("UPDATE people Set age = 100 WHERE name == 'Tom' ")
    # Обновить таблицу people, установить значение столбца age равным 100,
    # для тех записей в которых поле name имеет значение "Tom"
    con.commit()  # выполняем транзакцию


answer = ""
while True:  # бесконечный цикл разговора с пользователем
    answer = input("e - exit \n"
                   "s - show table\n"
                   "n - new data\n"
                   )
    if answer == "e":
        break

    if answer == "s":
        # извлекаем одну строку
        cursor.execute("SELECT * FROM people")
        while True:
            one_string = cursor.fetchone()
            if not one_string:
                break
            if one_string:
                print(one_string)
                #  print(type(one_string))
                #  if "Max" in one_string:
                #      print("Max in database")

    # вводим новые данные через консоль
    if answer == "n":
        new_name = input("enter new name ")
        new_age = input("enter new age ")
        new_execute = "INSERT INTO people (name, age) VALUES ('" + new_name + "', " + new_age + ")"
        print(new_execute)
        cursor.execute(new_execute)
        con.commit()

    print("\n")

con.close()
