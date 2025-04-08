import logging
from typing import Union

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(
    "C:/Users/2B/PycharmProjects/HomeWorkPoetry/logs/masks.log", encoding="utf-8", mode="w"
)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[str]) -> str:
    """маскирование номера карты в формат XXXX XX** **** XXXX, где X — это цифра номера"""

    if not isinstance(card_number, str):
        logger.error("Неверные тип входных данных")
        raise TypeError("Ошибка данных")

    if len(card_number) == 16:
        logger.info("Старт операции маскирования номера карты")
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        logger.error(f"Неверный формат Карты: количество символов - {len(card_number)}, значение: {card_number}")
        raise ValueError("Неверный формат Карты")


def get_mask_account(account_number: Union[str]) -> str:
    """маскирование номера счета в формат **XXXX, где X — это цифра номера"""
    if not isinstance(account_number, str):
        raise TypeError("Ошибка данных")

    if len(account_number) == 20:
        logger.info("Старт операции маскирования номера счета")
        return f"**{account_number[-4:]}"
    else:
        logger.error(f"Неверный формат Счета: количество символов - {len(account_number)}, значение: {account_number}")
        raise ValueError("Неверный формат Счета")
