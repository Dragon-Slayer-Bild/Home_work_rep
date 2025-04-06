import json
import os
from src.external_api import convert_currency


# путь относительный (filename="operations.json", dirname="C:\\Users\\2B\\PycharmProjects\\HomeWorkPoetry\\data")
def transactions_sum(filename="operations.json", dirname="data"):
    '''Сумма транзакций в рублях, с вызовом функции convert_currency для переконвертивония иностранной валюты в рубли'''
    file_path = os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), dirname), filename)
    result = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as transactions_file:
            transactions_data = json.load(transactions_file)
        for transaction in transactions_data:
            currency_from = transaction['operationAmount']['currency']['code']
            currency_to = 'RUB'
            amount = transaction['operationAmount']['amount']
            try:
                amount_float = round(float(amount.replace(',', '.')), 2)
            except ValueError:
                raise ValueError(f"Неверный тип суммы: {amount}. Сумма должна быть числом.")

            if currency_from == 'RUB':
                result += amount_float
            elif currency_from != 'RUB':
                convert_amount = convert_currency(currency_to, currency_from, amount_float)
                result += convert_amount
            else:
                return 'Ошибка проверки данных'
        return result
    except FileNotFoundError:
        raise FileNotFoundError(f"Ошибка: Файл '{filename}' не найден в папке '{dirname}'.")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Ошибка: Файл '{filename}' не содержит валидный JSON. {e}")
    except Exception as e:
        raise Exception(f"Произошла ошибка при чтении файла: {e}")
