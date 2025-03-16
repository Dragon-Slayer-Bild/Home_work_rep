from typing import Union


def get_mask_card_number(card_number: Union[str]) -> str:
    """маскирование номера карты в формат XXXX XX** **** XXXX, где X — это цифра номера"""
    if not isinstance(card_number, str):
        raise TypeError("Ошибка данных")

    if len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        raise ValueError("Неверный формат Карты")


def get_mask_account(account_number: Union[str]) -> str:
    """маскирование номера счета в формат **XXXX, где X — это цифра номера"""
    if not isinstance(account_number, str):
        raise TypeError("Ошибка данных")

    if len(account_number) == 20:
        return f"**{account_number[-4:]}"
    else:
        raise ValueError("Неверный формат Счета")
