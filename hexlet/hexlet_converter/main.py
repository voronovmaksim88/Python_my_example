from onlinerequuests import get_all_currencies
from onlinerequuests import convert_currency

print("Можно использовать следующие валюты")
all_currencies = get_all_currencies()
count = 1
for key in all_currencies.keys():
    print(f"{count}. {key}")
    count += 1

user_currency = input('Введите имеющуюся валюту: ')
user_amount = float(input('Введите сумму: '))
conversion_currency = input('Введите конвертную валюту: ')

result = user_amount * convert_currency(conversion_currency, user_currency)
print(round(result, 2))
