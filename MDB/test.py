import pyodbc

print(pyodbc.drivers())

conn_str = (
    r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
    r"DBQ=D:\YandexDisk\db\Data_Base_Sibplc_v13.mdb"
)
cnxn = pyodbc.connect(conn_str)
cursor = cnxn.cursor()
# SQL запрос на выбор всех строк из таблицы "MyTable"
cursor.execute("SELECT * FROM Box")

for row in cursor.fetchall():
    print(row)

cursor.close()
cnxn.close()

"""
Для чтения данных из файла базы данных Microsoft Access (.mdb) при помощи Python вы можете использовать пакет `pyodbc`.
Он позволяет подключаться к ODBC-совместимым базам данных при помощи SQL и предоставляет простой и удобный интерфейс
для работы с ними.

Шаг 1: Установите pyodbc
Установите pyodbc, используя pip:
pip install pyodbc

Шаг 2: Установите драйвер Microsoft Access
Драйверы позволяют приложениям взаимодействовать с базой данных.
Чтобы установить последний драйвер Microsoft Access в Windows 10, скачайте его и установите. 
Ссылка на скачивание: https://www.microsoft.com/en-us/download/details.aspx?id=54920

Шаг 3: Импорт pyodbc и подключение к базе данных
import pyodbc 

conn_str = (
    r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
    r"DBQ=path_to_your_database_file;"
)

cnxn = pyodbc.connect(conn_str)

Примечание: замените "path_to_your_database_file" на путь к вашему файлу .mdb.

Шаг 4: Чтение данных с помощью SQL запроса
cursor = cnxn.cursor()

# SQL запрос на выбор всех строк из таблицы "MyTable"
cursor.execute("SELECT * FROM MyTable")

for row in cursor.fetchall():
    print (row)


Этот код возвращает все строки из таблицы "MyTable" и затем выводит результаты по одной строке за раз.
Замените "MyTable" на имя таблицы, из которой вы хотите извлечь данные.

Шаг 5: Закрытие соединения
После окончания работы с базой данных всегда следует закрывать соединение.

cursor.close()
cnxn.close()

Примечание: доступ к базе данных зависит от уровня доступа пользователя к базе данных и файлу базы данных.
Если вы столкнетесь с проблемами доступа, убедитесь, что у вас есть необходимые разрешения.

"""
