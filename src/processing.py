import re
from collections import Counter
from datetime import datetime
from typing import Dict


def filter_by_state(state_list: list[dict], *, state: str = "EXECUTED") -> list[dict]:
    """Фильтрует список операций по статусу операции(по умолчанию статус = EXECUTED)"""
    filtered_list = []
    count = 0

    for element in state_list:
        if element.get("state") == state:
            filtered_list.append(element)
            count += 1
        else:
            None

    if count == 0:
        return []

    return filtered_list


def sort_by_date(date_state_list: list[dict], *, reverse: bool = True) -> str | list[dict]:
    """Сортирует список операций по дате (по умолчанию — убывание)"""
    filtered_date_list = sorted(
        date_state_list, key=lambda x: datetime.fromisoformat(x["date"].replace("Z", "+00:00")), reverse=reverse
    )
    return filtered_date_list


def transaction_search(transactions_list: list[dict], search_string: str) -> str | list[dict]:
    """Поиск транзакции  по описанию"""
    try:
        transactions = [
            transaction
            for transaction in transactions_list
            if re.findall(search_string, transaction["description"], flags=re.IGNORECASE)
        ]
        return transactions

    except TypeError:
        return "Неверный формат операций, должен быть список"


def transaction_count(transactions_list: list[dict], category_list: list):
    """Количество транзакций по категориям"""

    category_counts: Dict[str, int] = {category: 0 for category in category_list}
    counts_list = []

    for transaction in transactions_list:
        description = transaction.get("description", "")
        for category in category_list:
            if category.lower() in description.lower():
                counts_list.append(category)

    counts = Counter(counts_list)

    for category in category_list:
        category_counts[category] = counts[category]

    return category_counts
