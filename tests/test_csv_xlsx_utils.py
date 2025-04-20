import csv
import os

import pandas as pd
import pytest

from src.csv_xlsx_utils import transactions_list_from_csv_file, transactions_list_from_xlsx_file

TEST_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_data")


@pytest.fixture
def mock_csv_transactions_file(tmp_path):
    filename = "transactions_test.csv"
    file_path = tmp_path / filename
    data = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": "29740",
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
    ]
    fieldnames = ["id", "state", "date", "amount", "currency_name", "currency_code", "from", "to", "description"]
    with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        writer.writerows(data)
    return str(file_path)


@pytest.fixture
def mock_xlsx_transactions_file(tmp_path):
    filename = "transactions_test.xlsx"
    file_path = tmp_path / filename
    data = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": "29740",
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
    ]
    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False)
    return str(file_path)


def test_transactions_list_from_csv_file_success(mock_csv_transactions_file):
    transactions = transactions_list_from_csv_file(
        filename=os.path.basename(mock_csv_transactions_file), dirname=os.path.dirname(mock_csv_transactions_file)
    )
    assert len(transactions) == 2
    assert transactions[0]["id"] == "650703"
    assert transactions[0]["amount"] == "16210"
    assert transactions[0]["currency_code"] == "PEN"


def test_transactions_list_from_csv_file(tmp_path):
    """Файл не найден."""
    result = transactions_list_from_csv_file(filename="ololol.xlsx", dirname=str(tmp_path))
    assert result == []


def test_transactions_list_from_xlsx_file_success(mock_xlsx_transactions_file):
    transactions = transactions_list_from_xlsx_file(
        filename=os.path.basename(mock_xlsx_transactions_file), dirname=os.path.dirname(mock_xlsx_transactions_file)
    )
    assert len(transactions) == 2
    assert transactions[0]["id"] == 650703
    assert transactions[0]["amount"] == 16210
    assert transactions[0]["currency_code"] == "PEN"


def test_transactions_list_from_xlsx_file(tmp_path):
    """Файл не найден."""
    result = transactions_list_from_xlsx_file(filename="ololol.csv", dirname=str(tmp_path))
    assert result == []
