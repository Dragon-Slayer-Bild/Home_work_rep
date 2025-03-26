from typing import Iterator, Generator

def filter_by_currency(transactions: list, input_code: str) -> Iterator:
    """Функция поочередно выдает транзакции,где валюта операции соответствует заданной в input_code"""
    filtered_currency_list = filter(lambda x: x['operationAmount']['currency']['code'] == input_code, transactions)
    for i in filtered_currency_list:
        yield i


def transaction_descriptions(transactions: list[dict]) -> Generator[str, None, None]:
    """Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    if not transactions:
        raise ValueError("Передано пустое значение!")
    for item in transactions:
        if "description" not in item:
            yield 'Описание не найдено'
        else:
            yield item["description"]


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генератор, который возвращает номера банковских карт в формате XXXX XXXX XXXX XXXX
    """
    for number in range(start, end + 1):
        card_number = f"{number:016d}"
        formatted_card_number = " ".join(
            [card_number[i:i + 4] for i in range(0, 16, 4)]
        )
        yield formatted_card_number