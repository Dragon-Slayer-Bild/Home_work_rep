from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_account_number: Union[str]) -> str:
    """Маскирование номера счета или карты"""

    card_account_element = []
    card_account_number_split = card_account_number.split(" ")
    for element in card_account_number_split:
        if element.isdigit() is True and len(element) == 20:
            card_account_element.append(get_mask_account(element))
        elif element.isdigit() is True and len(element) == 16:
            card_account_element.append(get_mask_card_number(element))
        else:
            card_account_element.append(element)
    return " ".join(card_account_element)


def get_date(date: Union[str]) -> str:
    """Форматирование даты в формат ДД.ММ.ГГГГ"""
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"


card_account_number = "Visa Platinum 8990922113665229"
print(mask_account_card(card_account_number))
card_account_number = "Счет 35383033474447895560"
print(mask_account_card(card_account_number))
date = "2024-03-11T02:26:18.671407"
print(get_date(date))
