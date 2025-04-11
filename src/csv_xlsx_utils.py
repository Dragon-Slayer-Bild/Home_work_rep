import csv
import logging
import os

import pandas as pd

logger = logging.getLogger("csv_utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(
    "C:/Users/2B/PycharmProjects/HomeWorkPoetry/logs/csv_utils.log", encoding="utf-8", mode="w"
)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def transactions_list_from_csv_file(filename="transactions.csv", dirname="data") -> list:
    """
    Функция принимает путь с файлом с форматом csv, где хранятся операции и возвращает список этих операций

    """
    file_path = os.path.join(
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), dirname), filename
    )
    try:
        transactions_list_csv = []

        logger.info("Открытие файла с операциями в формате csv")
        with open(file_path, encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            logger.info("Запись транзакций в переменную")
            for row_csv in reader:
                transactions_list_csv.append(row_csv)
        return transactions_list_csv
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден в папке '{dirname}'.")
        logger.error(f"Ошибка: Файл '{filename}' не найден в папке '{dirname}'.")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        logger.error(f"Произошла ошибка при чтении файла: {e}")
        return []


logger = logging.getLogger("csv_utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(
    "C:/Users/2B/PycharmProjects/HomeWorkPoetry/logs/xlsx_utils.log", encoding="utf-8", mode="w"
)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def transactions_list_from_xlsx_file(filename="transactions_excel.xlsx", dirname="data") -> list:
    """
    Функция принимает путь с файлом с форматом xlsx, где хранятся операции и возвращает список этих операций
    """
    file_path = os.path.join(
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), dirname), filename
    )
    try:
        logger.info("Открытие файла с операциями в формате xlsx")
        excel_data = pd.read_excel(file_path)
        logger.info("Преобразование данных в словарь")
        dict_excel_data = excel_data.to_dict(orient="records")
        return dict_excel_data
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден в папке '{dirname}'.")
        logger.error(f"Ошибка: Файл '{filename}' не найден в папке '{dirname}'.")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        logger.error(f"Произошла ошибка при чтении файла: {e}")
        return []
