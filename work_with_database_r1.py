import pyodbc


# Создание подключения к базе данных
#conn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb,*.accdb)}; DBQ=D:/YandexDisk/db/Data_Base_Sibplc_v13.mdb;')
# con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=d:/YandexDisk/db/Data_Base_Sibplc_v13.mdb;')

'''
# Создание курсора для выполнения запросов
cur = con.cursor()

# Выполнение запроса
cur.execute('SELECT * FROM Box')

# Получение результатов
rows = cur.fetchall()
print(rows)

# Закрытие курсора и подключения
cur.close()
con.close()
'''