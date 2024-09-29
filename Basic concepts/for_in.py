# end = ''  это для того чтоб не переходить на новую строку

print("for")
# цикл For, для того чтоб пройтись по массиву
text = "abcdef"
for i in text:
    print(i.upper(), end='')

print("\n")
print("for выпиливаем букву")
text = "abcdef"
for i in text:
    if i == "b":
        print(end=' ')
        continue  # пропускаем итерацию
    print(i, end='')

print("\n")
print("for тормозим цикл")
text = "abcdef"
for i in text:
    if i == "e":
        break  # останавливаем цикл
    print(i * 2, end='')

print("")
print("")
# цикл For, для того чтоб пройтись словарю
my_PLC = {"Manufacturer": "Zentec", "Model": "M245", "Price": 10000}
for item in my_PLC.items():
    key, value = item
    print(key, value)

print("")
for k, v in my_PLC.items():
    print(k, v)

print("")
for n in range(0, 10, 2):
    print(n, end=', ')
