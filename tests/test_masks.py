import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def card_number() -> str:
    return "7000792289606361"


@pytest.fixture
def account_number() -> str:
    return "73654108430135874305"


def test_get_mask_card_number(card_number: str) -> None:
    assert get_mask_card_number(card_number) == "7000 79** **** 6361"


def test_get_mask_card_number_invalid_length() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number("1")


def test_get_mask_card_number_invalid_type() -> None:
    with pytest.raises(TypeError):
        get_mask_card_number(51)


def test_get_mask_account(account_number: str) -> None:
    assert get_mask_account(account_number) == "**4305"


def test_get_mask_account_number_invalid_length() -> None:
    with pytest.raises(ValueError):
        get_mask_account("12")


def test_get_mask_account_number_invalid_type() -> None:
    with pytest.raises(TypeError):
        get_mask_account(551)
