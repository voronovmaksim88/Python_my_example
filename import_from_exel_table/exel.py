# в этом примере считаем данные из талицы exel
import pandas as pd
import xlrd
# xlrd is a library for reading data and formatting information from Excel files in the historical .xls format.

df = pd.read_excel(r'Manufacturers.xls')

# Получение значения из конкретной ячейки по числовому индексу

value = df.keys()
print("keys", value)

value = df.columns
print("columns", value)

value = df.iloc[0, 0]
print(value)

value = df.iloc[0, 1]
print(value)

value = df.iloc[0, 2]
print(value)

# второй способ код ниже работает !!!
# import xlrd
print()
book = xlrd.open_workbook(r"Manufacturers.xls")
print("The number of worksheets is {0}".format(book.nsheets))
print("Worksheet name(s): {0}".format(book.sheet_names()))
sh = book.sheet_by_index(0)
print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
print("Cell С30 is {0}".format(sh.cell_value(rowx=29, colx=2)))
for rx in range(sh.nrows):
    print(sh.row(rx))
