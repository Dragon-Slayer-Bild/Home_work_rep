import requests
from dotenv import load_dotenv
import os

from typing import Union

load_dotenv()

api_key = os.getenv('API_KEY')


def convert_currency(currency_to: str, currency_from: str, amount: Union[int, float] ):
    '''вызов внешнего сервиса для конвертации валюты'''
    if not isinstance(amount, (int, float)):
        raise TypeError("Сумма должны быть int или float")

    if amount < 0:
        raise TypeError('Неверные входные данные')

    url = f'https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount={amount}'
    headers = {
        "apikey": api_key
    }
    response  = requests.get(url, headers=headers)
    response_json = response.json()
    status_code = response.status_code

    if status_code == 200:
        convert_result = round(float(response_json['result']), 2)
        return convert_result
    else:
        return (response_json['message'])
