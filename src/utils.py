import json
import logging
import os

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(
    "C:/Users/2B/PycharmProjects/HomeWorkPoetry/logs/utils.log", encoding="utf-8", mode="w"
)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


# путь относительный (filename="operations.json", dirname="C:\\Users\\2B\\PycharmProjects\\HomeWorkPoetry\\data")
def transactions_list_from_file(filename="operations.json", dirname="data") -> list:
    """
    Функция принимает путь с файлом, где хранятся операции и возвращает список этих операций
    """
    file_path = os.path.join(
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), dirname), filename
    )
    transactions_list = []
    try:
        logger.info("Открытие файла с операциями")
        with open(file_path, "r", encoding="utf-8") as transactions_file:
            transactions_data = json.load(transactions_file)
        logger.info("Запись транзакций в переменную")
        for transaction in transactions_data:
            transactions_list.append(transaction)
        return transactions_list
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден в папке '{dirname}'.")
        logger.error(f"Ошибка: Файл '{filename}' не найден в папке '{dirname}'.")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка: Файл '{filename}' не содержит валидный JSON. {e}")
        logger.error(f"Ошибка: Файл '{filename}' не содержит валидный JSON. {e}")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        logger.error(f"Произошла ошибка при чтении файла: {e}")
        return []


print(transactions_list_from_file())
