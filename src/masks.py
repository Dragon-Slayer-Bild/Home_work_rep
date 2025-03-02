from typing import Union


def get_mask_card_number(card_number: Union[str]) -> str:
    """маскирование номера карты в формат XXXX XX** **** XXXX, где X — это цифра номера"""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: Union[str]) -> str:
    """маскирование номера счета в формат **XXXX, где X — это цифра номера"""
    return f"**{account_number[-4:]}"


card_number = "7000792289606361"
print(get_mask_card_number(card_number))
account_number = "73654108430135874305"
print(get_mask_account(account_number))
