import pytest
from src.generators import filter_by_currency
from src.generators import transaction_descriptions
from src.generators import card_number_generator


@pytest.fixture
def transaction_list():
    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]
    return transactions


def test_filter_by_currency(transaction_list):
    """Тест на корретность списка всех транзакций с выбранной валютой"""
    usd_transactions = filter_by_currency(transaction_list, "USD")
    result = list(usd_transactions)
    expected_transactions = [
        {
            "date": "2018-06-30T02:08:58.425572",
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "id": 939719570,
            "operationAmount": {"amount": "9824.07", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 11776614605963066702",
        },
        {
            "date": "2019-04-04T23:20:05.206878",
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "id": 142264268,
            "operationAmount": {"amount": "79114.93", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 75651667383060284188",
        },
        {
            "date": "2018-08-19T04:27:37.904916",
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "id": 895315941,
            "operationAmount": {"amount": "56883.54", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Visa Platinum 8990922113665229",
        },
    ]
    assert result == expected_transactions


def test_filter_by_currency(transaction_list):
    """Тест на корректность получения первой транзакции с выбранной валютой из генератора"""
    usd_transactions = filter_by_currency(transaction_list, "USD")
    result = next(usd_transactions)
    expected_transactions = {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert result == expected_transactions


@pytest.mark.parametrize(
    "input_code, expected_transactions",
    [
        (
            "USD",
            [
                {
                    "date": "2018-06-30T02:08:58.425572",
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "id": 939719570,
                    "operationAmount": {"amount": "9824.07", "currency": {"code": "USD", "name": "USD"}},
                    "state": "EXECUTED",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "date": "2019-04-04T23:20:05.206878",
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "id": 142264268,
                    "operationAmount": {"amount": "79114.93", "currency": {"code": "USD", "name": "USD"}},
                    "state": "EXECUTED",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "date": "2018-08-19T04:27:37.904916",
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "id": 895315941,
                    "operationAmount": {"amount": "56883.54", "currency": {"code": "USD", "name": "USD"}},
                    "state": "EXECUTED",
                    "to": "Visa Platinum 8990922113665229",
                },
            ],
        ),
        (
            "RUB",
            [
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                },
            ],
        ),
    ],
)
def test_filter_by_currency_data_parametrize(transaction_list, input_code, expected_transactions):
    """Тест с несколькими параметрами валюты"""
    result = list(filter_by_currency(transaction_list, input_code))
    assert result == expected_transactions


def test_filter_by_currency_empty_transactions(transaction_list):
    """Тест на пустой список транзакций"""
    result = list(filter_by_currency([], "USD"))
    assert result == []


def test_filter_by_currency_currency_not_found(transaction_list):
    """Тест, когда валюта не найдена в списке транзакций."""
    result = list(filter_by_currency(transaction_list, "JPY"))
    assert result == []


def test_transaction_descriptions(transaction_list):
    """Тест на корректность получения описания из генератора"""
    transaction_description = transaction_descriptions(transaction_list)
    result = next(transaction_description)
    expected_description = "Перевод организации"
    assert result == expected_description


def test_missing_description_returns_default_message():
    """Тест: Если отсутствует ключ 'description', возвращается 'Описание не найдено'."""
    transactions = [
        {"description": "Покупка в магазине"},
        {},
        {"description": "Перевод организации"},
    ]
    expected_descriptions = ["Покупка в магазине", "Описание не найдено", "Перевод организации"]
    result = list(transaction_descriptions(transactions))
    assert result == expected_descriptions


def test_empty_list_raises_value_error():
    """Пустой список должен вызывать ValueError."""
    with pytest.raises(ValueError) as excinfo:
        list(transaction_descriptions([]))
    assert str(excinfo.value) == "Передано пустое значение!"


def test_card_number_generator():
    """Тест с одним числом в диапазоне."""
    result = list(card_number_generator(1, 1))
    assert result == ["0000 0000 0000 0001"]


def test_card_number_generator_mult_numbers():
    """Тест с несколькими числами в диапазоне."""
    result = list(card_number_generator(1, 3))
    assert result == ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]


def test_end_equal_to_max_16_digit_number():
    """Тест, когда end равно максимальному 16-значному числу."""
    result = list(card_number_generator(9999999999999999, 9999999999999999))
    assert result == ["9999 9999 9999 9999"]
