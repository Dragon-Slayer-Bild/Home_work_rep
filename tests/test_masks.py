import pytest

from src.masks import get_mask_account
from src.masks import get_mask_card_number

@pytest.fixture
def card_number():
    return "7000792289606361"

@pytest.fixture
def account_number():
    return "73654108430135874305"


def test_get_mask_card_number(card_number):
    assert get_mask_card_number(card_number) == '7000 79** **** 6361'


def test_get_mask_card_number_invalid_length():
    with pytest.raises(ValueError):
        get_mask_card_number('1')


def test_get_mask_card_number_invalid_type():
    with pytest.raises(TypeError):
        get_mask_card_number(551)


def test_get_mask_account(account_number):
    assert get_mask_account(account_number) == '**4305'


def test_get_mask_account_number_invalid_length():
    with pytest.raises(ValueError):
        get_mask_account('12')


def test_get_mask_account_number_invalid_type():
    with pytest.raises(TypeError):
        get_mask_account(551)
