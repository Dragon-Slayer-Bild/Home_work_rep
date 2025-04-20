from src.csv_xlsx_utils import transactions_list_from_csv_file, transactions_list_from_xlsx_file
from src.generators import filter_by_currency, transaction_descriptions
from src.processing import filter_by_state, sort_by_date, transaction_search
from src.utils import transactions_list_from_file
from src.widget import get_date, mask_account_card


def main():
    """Основная функция для взаимодействия с пользователем, внутри себя ссылается на другие функции проекта"""
    global transaction_list_by_status_date

    print("\nПривет! Добро пожаловать в программу работы с банковскими транзакциями.\n")

    while True:
        file_input = input(
            "Выберите необходимый пункт меню:\n"
            "1. Получить информацию о транзакциях из JSON-файла\n"
            "2. Получить информацию о транзакциях из CSV-файла\n"
            "3. Получить информацию о транзакциях из XLSX-файла\n"
        )

        if file_input == "1":
            print("Для обработки выбран JSON-файл.\n")
            # получение списка транзакций из файла JSON
            transaction_list = list[dict](transactions_list_from_file())
            break

        elif file_input == "2":
            print("Для обработки выбран CSV-файла.\n")
            # получение списка транзакций из файла CSV
            transaction_list = transactions_list_from_csv_file()
            break

        elif file_input == "3":
            print("Для обработки выбран XLSX-файла.\n")
            # получение списка транзакций из файла XLSX
            transaction_list = transactions_list_from_xlsx_file()
            break

        else:
            print("Неверно. Выберите пункт из предложенного списка\n")

    while True:
        status_input = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
        )

        if status_input.upper() == "EXECUTED":
            print('\nОперации отфильтрованы по статусу "EXECUTED"\n')
            # фильтр списка транзакций по статусу EXECUTED
            transaction_list_by_status = filter_by_state(transaction_list, state="EXECUTED")
            break

        elif status_input.upper() == "CANCELED":
            print('\nОперации отфильтрованы по статусу "CANCELED"\n')
            # фильтр списка транзакций по статусу CANCELED
            transaction_list_by_status = filter_by_state(transaction_list, state="CANCELED")
            break

        elif status_input.upper() == "PENDING":
            print('\nОперации отфильтрованы по статусу "PENDING"\n')
            # фильтр списка транзакций по статусу PENDING
            transaction_list_by_status = filter_by_state(transaction_list, state="PENDING")
            break

        else:
            print(f"\nСтатус операции {status_input} недоступен.\n")

    while True:
        date_input = input("Отсортировать операции по дате? Да/Нет\n")

        if date_input.lower() == "да":
            while True:
                date_filter_input = input("Отсортировать по возрастанию или по убыванию?\n")

                if date_filter_input.lower() == "по возрастанию":
                    # фильтр списка транзакций по возврастанию
                    transaction_list_by_status_date = sort_by_date(transaction_list_by_status)
                    break

                elif date_filter_input.lower() == "по убыванию":
                    # фильтр списка транзакций по убыванию
                    transaction_list_by_status_date = sort_by_date(transaction_list_by_status, reverse=False)
                    break

                else:
                    print("\nНеверно. Выберите пункт из предложенного фильтра\n")

            break

        elif date_input.lower() == "нет":
            # Не фильтруем список по дате и присваиваем значение предыдущей фильтрации по статусу
            transaction_list_by_status_date = transaction_list_by_status
            break

        else:
            print("\nНеверно. Выберите пункт из предложенного фильтра\n")

    while True:
        currency_input = input("Выводить только рублевые транзакции? Да/Нет\n")

        if currency_input.lower() == "да":
            currency_code = "RUB"
            # осуществляем вызов генератора для получения списка транзакций по валюте
            transaction_list_by_status_date_currency_gen = filter_by_currency(
                transaction_list_by_status_date, input_code=currency_code
            )
            transaction_list_by_status_date_currency = []
            for transaction in transaction_list_by_status_date_currency_gen:
                transaction_list_by_status_date_currency.append(transaction)
            print(transaction_list_by_status_date_currency)
            break

        elif currency_input.lower() == "нет":
            # осуществляем вызов генератора для получения назначения платежа
            transaction_list_by_status_date_currency = transaction_list_by_status
            print(transaction_list_by_status_date_currency)
            break

        else:
            print("\nНеверно. Выберите пункт из предложенного фильтра\n")

    while True:
        word_input = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")

        if word_input.lower() == "да":
            descriptions = transaction_descriptions(transaction_list_by_status_date_currency)

            word_input_search = input("Введите слово\n")

            filtered_transactions = transaction_search(transaction_list_by_status_date_currency, word_input_search)
            formatted_transactions = []
            count = 0

            try:
                # из списка транзакций формируем необходимые переменые для списка формирования необходимого формата
                for get_transaction, description in zip(filtered_transactions, descriptions):
                    formatted_date = get_date(get_transaction["date"])
                    pay_from = mask_account_card(get_transaction.get("from", ""))
                    pay_to = mask_account_card(get_transaction.get("to", ""))
                    try:
                        amount = get_transaction["operationAmount"]["amount"]
                    except KeyError:
                        amount = get_transaction.get("amount")
                    try:
                        currency = get_transaction["operationAmount"]["currency"]["code"]
                    except KeyError:
                        currency = get_transaction.get("currency_code")
                    formatted_transactions.append(
                        f"\n{formatted_date} {description}\n{pay_from} -> {pay_to}\n{amount} {currency}"
                    )
                    count += 1

            except StopIteration:
                print("Закончились транзакции или описания.")

            print("Распечатываю итоговый список транзакций...")

            if len(formatted_transactions) > 0:
                print(f"Всего банковских операций в выборке: {len(formatted_transactions)}")
                print("\n".join(formatted_transactions))
                break

            else:
                print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
                break

        elif word_input.lower() == "нет":
            # осуществляем вызов генератора для получения назначения платежа
            descriptions = transaction_descriptions(transaction_list_by_status_date_currency)

            formatted_transactions = []
            count = 0

            try:
                # из списка транзакций формируем необходимые переменые для списка формирования необходимого формата
                for get_transaction, description in zip(transaction_list_by_status_date_currency, descriptions):
                    print(count)
                    formatted_date = get_date(get_transaction["date"])
                    pay_from = mask_account_card(get_transaction.get("from", ""))
                    pay_to = mask_account_card(get_transaction.get("to", ""))
                    try:
                        amount = get_transaction["operationAmount"]["amount"]
                    except KeyError:
                        amount = get_transaction.get("amount")
                    try:
                        currency = get_transaction["operationAmount"]["currency"]["code"]
                    except KeyError:
                        currency = get_transaction.get("currency_code")
                    formatted_transactions.append(
                        f"\n{formatted_date} {description}\n{pay_from} -> {pay_to}\n{amount} {currency}"
                    )
                    count += 1

            except StopIteration:
                print("Закончились транзакции или описания.")

            print("Распечатываю итоговый список транзакций...")

            if len(formatted_transactions) > 0:
                print(f"Всего банковских операций в выборке: {len(formatted_transactions)}")
                print("\n".join(formatted_transactions))
                break

            else:
                print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
                break

        else:
            print("\nНеверно. Выберите пункт из предложенного фильтра\n")


print(main())
