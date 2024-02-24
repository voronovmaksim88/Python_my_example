def print_table(data, cell_sep=' | ', header_separator=True):
    rows = len(data)
    cols = len(data[0])

    col_width = []
    for col in range(cols):
        columns = [data[row][col] for row in range(rows)]
        col_width.append(len(max(columns, key=len)))

    separator = "-+-".join('-' * n for n in col_width)

    for i, row in enumerate(range(rows)):
        if i == 1 and header_separator:
            print(separator)

        result = []
        for col in range(cols):
            item = data[row][col].rjust(col_width[col])
            result.append(item)

        print(cell_sep.join(result))


table1 = [["column1", "column2", "column3"], ["data1", "data2", "data3"]]  # список списков
table2 = (("column1", "column2", "column3", "column4"), ("data1", "data2", "data3", "data4"))  # кортеж кортежей
print_table(table1)
print()
print_table(table2)
