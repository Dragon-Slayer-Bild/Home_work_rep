import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card_account_number, expected",
    [
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ],
)
def test_mask_account_card(card_account_number: str, expected: str) -> None:
    assert mask_account_card(card_account_number) == expected


@pytest.mark.parametrize("card_account_number", ["Visa Platinum 89XX13665229", "Счет 3538347X2895560"])
def test_mask_account_card_invalid_value(card_account_number: str) -> None:
    with pytest.raises(ValueError):
        mask_account_card(card_account_number)


def test_mask_account_card_invalid_type() -> None:
    with pytest.raises(ValueError):
        mask_account_card(-1)


@pytest.fixture
def date_value() -> str:
    return "2024-03-11T02:26:18.671407"


def test_get_date(date_value: str) -> None:
    assert get_date(date_value) == "11.03.2024"


def test_get_date_empty() -> None:
    with pytest.raises(ValueError):
        get_date("")
