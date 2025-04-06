import json
import os
from unittest.mock import patch
import pytest
from src.utils import transactions_sum

TEST_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_data')

@pytest.fixture
def mock_transactions_file(tmp_path):
    """Создает временный файл transactions.json с тестовыми данными."""
    data = [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  },
  {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
      "amount": "9824.07",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
  }    ]
    json_data = json.dumps(data)
    file_path = tmp_path / "operations.json"
    file_path.write_text(json_data, encoding='utf-8')
    return file_path

def test_transactions_sum_rub_only(tmp_path):
    """Только транзакции в рублях."""
    file_path = tmp_path / "operations.json"
    file_path.write_text(json.dumps([{"operationAmount": {"currency": {"code": "RUB"}, "amount": "100.00"}},
        {"operationAmount": {"currency": {"code": "RUB"}, "amount": "200.00"}}]), encoding='utf-8')
    result = transactions_sum(filename="operations.json", dirname=str(tmp_path))
    assert result == 300.0


def test_transactions_sum_usd_and_eur(tmp_path):
    """Тест с валютами USD и EUR, мокирование convert_currency."""
    file_path = tmp_path / "operations.json"
    file_path.write_text(json.dumps([{"operationAmount": {"currency": {"code": "USD"}, "amount": "200.00"}},
        {"operationAmount": {"currency": {"code": "EUR"}, "amount": "300.00"}}]), encoding='utf-8')

    with patch('src.utils.convert_currency') as mock_convert_currency:
        mock_convert_currency.side_effect = lambda to, fr, amount: amount * 70 if fr == 'USD' else amount * 80
        result = transactions_sum(filename="operations.json", dirname=str(tmp_path))
        assert result == 200.0 * 70 + 300.0 * 80


def test_transactions_sum_file_not_found(tmp_path):
    """Файл не найден."""
    with pytest.raises(FileNotFoundError, match="Ошибка: Файл 'nonexistent.json' не найден"):
        transactions_sum(filename="nonexistent.json", dirname=str(tmp_path))