def filter_by_state(state_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтрует список операций по статусу операции(по умолчанию статус = EXECUTED)"""
    filtered_list = []
    for element in state_list:
        if state == element["state"]:
            filtered_list.append(element)
        else:
            None
    return filtered_list


def sort_by_date(date_state_list: list[dict], reverse: bool = True) -> list[dict]:
    """Сортирует список операций по дате (по умолчанию — убывание)"""
    filtered_date_list = sorted(date_state_list, key=lambda x: x["date"], reverse=reverse)
    return filtered_date_list


state_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
print(filter_by_state(state_list, "CANCELED"))
print(filter_by_state(state_list))
print(sort_by_date(state_list))
print(sort_by_date(state_list, False))
