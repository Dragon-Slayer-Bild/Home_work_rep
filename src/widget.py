from datetime import datetime
from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_account_number: Union[str]) -> str:
    """Маскирование номера счета или карты"""

    card_account_element = []

    if not isinstance(card_account_number, str):
        try:
            card_account_number = str(card_account_number)
        except Exception:
            raise TypeError("неверный тип данных")

    if not card_account_number:
        return ""

    card_account_number_split = card_account_number.split(" ")
    for element in card_account_number_split:
        if element.isdigit() and len(element) == 20:
            card_account_element.append(get_mask_account(element))
        elif element.isdigit() and len(element) == 16:
            card_account_element.append(get_mask_card_number(element))
        elif element.isalpha():
            card_account_element.append(element)
        else:
            raise ValueError("неверный формат")
    return " ".join(card_account_element)


def get_date(date_unformate: str) -> str:
    """Форматирование даты в формат ДД.ММ.ГГГГ"""
    try:
        date_string_iso = date_unformate.replace("Z", "+00:00")
        formatted_date = datetime.fromisoformat(date_string_iso)
        return formatted_date.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Некорректный формат даты")
