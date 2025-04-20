from typing import Dict

import pytest

from src.processing import filter_by_state, sort_by_date, transaction_count, transaction_search


@pytest.fixture
def state_list_value() -> list[dict]:
    state_list = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 939719571, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    return state_list


@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 939719571, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
    ],
)
def test_filter_by_state(state_list_value: list[dict], expected: list[dict], state: str) -> None:
    assert filter_by_state(state_list_value, state=state) == expected


def test_filter_by_invalid_state() -> None:
    result = filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 939719571, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        state="EXsdasdaECUTEDsss",
    )

    expected = []
    assert result == expected


@pytest.mark.parametrize(
    "reverse, expected",
    [
        (
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 939719571, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 939719571, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date(state_list_value: list[dict], expected: list[dict], reverse: bool) -> None:
    assert sort_by_date(state_list_value, reverse=reverse) == expected


@pytest.mark.parametrize(
    "invalid_date",
    [
        (
            {"id": 41428829, "state": "EXECUTED", "date": "2025-07-03"},
            {"id": 615064591, "state": "CANCELED", "date": "18:35:29.512364"},
            {"id": 939719571, "state": "EXECUTED", "date": "03-07-2019T18:35:29"},
        )
    ],
)
def test_sort_by_invalid_date(invalid_date: list[dict]) -> None:
    with pytest.raises(ValueError):
        sort_by_date(invalid_date)


def test_transaction_search_valid_search():
    transactions = [
        {"description": "Покупка в магазине"},
        {"description": "Оплата интернета"},
        {"description": "Перевод другу"},
    ]
    search_string = "покупка"
    result = transaction_search(transactions, search_string)
    assert len(result) == 1
    assert result[0]["description"] == "Покупка в магазине"


def test_transaction_search_no_match():
    transactions = [
        {"description": "Покупка в магазине"},
        {"description": "Оплата интернета"},
        {"description": "Перевод другу"},
    ]
    search_string = "кафе"
    result = transaction_search(transactions, search_string)
    assert len(result) == 0


def test_transaction_search_invalid_transactions_list():
    transactions_list = "ololo"
    search_string = "покупка"
    result = transaction_search(transactions_list, search_string)
    assert result == "Неверный формат операций, должен быть список"


def test_transaction_search_empty_list():
    transactions = []
    search_string = "покупка"
    result = transaction_search(transactions, search_string)
    assert len(result) == 0


def test_transaction_count_basic():
    transactions = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "КАТА 1",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "КАТА 2",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "КАТА 2",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "д",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
    ]
    category_list = ["КАТА 1", "КАТА 2", "д"]
    expected_counts = {"КАТА 1": 1, "КАТА 2": 2, "д": 1}
    assert transaction_count(transactions, category_list) == expected_counts


def test_transaction_count_empty_categories():
    transactions = [
        {"description": "Покупка продуктов"},
        {"description": "Оплата интернета"},
    ]
    categories = []
    expected_counts: Dict[str, int] = {}
    assert transaction_count(transactions, categories) == expected_counts


def test_transaction_count_empty_transactions():
    transactions = []
    categories = ["продукты", "интернет"]
    expected_counts = {"продукты": 0, "интернет": 0}
    assert transaction_count(transactions, categories) == expected_counts


def test_transaction_count_missing_description():
    transactions = [
        {"amount": 100},  # нет описания
        {"description": "Оплата интернета"},
    ]
    categories = ["продукты", "интернет"]
    expected_counts = {"продукты": 0, "интернет": 1}
    assert transaction_count(transactions, categories) == expected_counts
