from src.external_api import convert_currency
from unittest.mock import Mock,patch
import os
import pytest

@patch('requests.get')
def test_convert_currency(mock_get):
    mock_json_result = {
  "date": "2018-02-22",
  "historical": "",
  "info": {
    "rate": 101,
    "timestamp": 1519328414
  },
  "query": {
    "amount": 8221.37,
    "from": "USD",
    "to": "RUB"
  },
  "result": 697457.16222,
  "success": True
}
    mock_json = Mock(return_value=mock_json_result)
    mock_get.return_value.json = mock_json
    mock_get.return_value.status_code = 200

    assert convert_currency('RUB', 'USD', 8221.37) == 697457.16

    expected_url = 'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=8221.37'
    mock_get.assert_called_with(expected_url, headers={"apikey": os.getenv('API_KEY')})
    mock_json.assert_called()


@patch('requests.get')
def test_convert_currency_invalid_api_key(mock_get):
    mock_get.return_value.json.return_value = {"message": "Invalid API Key"}
    result = convert_currency('RUB', 'USD', 8221.37)
    assert result == "Invalid API Key"


def test_convert_currency_invalid_amount():
  with pytest.raises(TypeError):
      convert_currency('RUB', 'USD', -8221.3)