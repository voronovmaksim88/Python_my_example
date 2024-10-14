import requests
from pprint import pprint

API_KEY = 'fca_live_DUxLeYRJST6PJ3mhyQPhM3gZVAbeEz5c8qaVHRC3'


def convert_currency(from_currency, to_currency):
    url = (f"https://api.freecurrencyapi.com/v1/latest?apikey="
           f"{API_KEY}&currencies={from_currency}&base_currency={to_currency}")
    responce = requests.get(url)  # запрос к API
    data_info = responce.json()  # получаем данные в виде словаря
    currency = data_info.get('data', None)
    val = currency.get(from_currency, None)
    print(f'Курс {from_currency} в {to_currency} равен {val}')
    return round(val, 2)


print(convert_currency(from_currency='RUB', to_currency='EUR'))


def get_all_currencies():
    all_currencies_url = f"https://api.freecurrencyapi.com/v1/currencies?apikey={API_KEY}&currencies=&base_currency"
    response = requests.get(url=all_currencies_url)
    # print(response.json())
    all_currencies = response.json().get('data', None)

    # pprint(all_currencies)

    # for key, value in all_currencies.items():
    #     print(key)
    return all_currencies


get_all_currencies()
