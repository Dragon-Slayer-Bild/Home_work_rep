import os

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")


def convert_currency(transaction: dict) -> float:
    """
    функция для вывода суммы из операции в рублях,
    если операция в иностранной валюте происходит
    вызов внешнего api для пересчета суммы ин. валюты в рубли
    """
    amount = float(transaction["operationAmount"]["amount"])
    transaction_currency = transaction["operationAmount"]["currency"]["code"]

    if not isinstance(amount, (int, float)):
        raise TypeError("Сумма должны быть int или float")

    if amount < 0:
        raise TypeError("Неверные входные данные")

    if transaction_currency == "RUB":
        return round(float(amount), 2)
    else:
        currency_to = "RUB"
        currency_from = transaction_currency

        url = (
            f"https://api.apilayer.com/exchangerates_data/convert?to="
            f"{currency_to}&from={currency_from}&amount={amount}"
        )
        headers = {"apikey": api_key}

        response = requests.get(url, headers=headers)
        response_json = response.json()
        status_code = response.status_code

        if status_code == 200:
            convert_result = round(float(response_json["result"]), 2)
            return convert_result
        else:
            return response_json["message"]
