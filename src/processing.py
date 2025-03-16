from datetime import datetime


def filter_by_state(state_list: list[dict], *, state: str = "EXECUTED") -> list[dict]:
    """Фильтрует список операций по статусу операции(по умолчанию статус = EXECUTED)"""
    filtered_list = []
    count = 0

    for element in state_list:
        if state == element["state"]:
            filtered_list.append(element)
            count += 1
        else:
            None

    if count == 0:
        raise ValueError(f"Статуса {state} не существует")

    return filtered_list


def sort_by_date(date_state_list: list[dict], *, reverse: bool = True) -> list[dict]:
    """Сортирует список операций по дате (по умолчанию — убывание)"""
    filtered_date_list = sorted(
        date_state_list, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=reverse
    )
    return filtered_date_list
