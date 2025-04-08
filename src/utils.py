import json
import os


# путь относительный (filename="operations.json", dirname="C:\\Users\\2B\\PycharmProjects\\HomeWorkPoetry\\data")
def transactions_list_from_file(filename="operations3.json", dirname="data") -> list:
    """
    Функция принимает путь с файлом, где хранятся операции и возвращает список этих операций
    """
    file_path = os.path.join(
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), dirname), filename
    )
    transactions_list = []
    try:
        with open(file_path, "r", encoding="utf-8") as transactions_file:
            transactions_data = json.load(transactions_file)
        for transaction in transactions_data:
            transactions_list.append(transaction)
        return transactions_list
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден в папке '{dirname}'.")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка: Файл '{filename}' не содержит валидный JSON. {e}")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        return []
