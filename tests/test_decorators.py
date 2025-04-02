from src.decorators import log
import pytest


@pytest.fixture
def sum_func():
    """Тестовая функция сложения, декорированная log с выводом в консоль"""
    @log()
    def inner_sum(x: int, y: int) -> int:
        '''Реальная функция сложения'''
        return x + y
    return inner_sum


@pytest.fixture
def sum_func_with_file():
    """Тестовая функция сложения, декорированная log с сохранением в файл."""
    @log(filename="mylog.txt")
    def inner_sum_with_file(x: int, y: int) -> int:
        '''Реальная функция сложения'''
        return x + y
    return inner_sum_with_file


def test_sum_func_log(capsys, sum_func):
    """Тест для проверки логирования функции sum_func."""
    result = sum_func(1, 2)

    assert result == 3
    captured = capsys.readouterr()
    assert '[inner_sum] result: 3 - OK' in captured.out


def test_sum_func_log_with_file(sum_func_with_file):
    """Тест для проверки логирования функции sum_func."""
    result = sum_func_with_file(1, 4)

    assert result == 5
    with open('mylog.txt', "r") as f:
        log_text = f.read()

    assert "[inner_sum_with_file] result: 5 - OK" in log_text


def test_sum_func_log_error(capsys, sum_func):
    """Тест для проверки логирования функции sum_func."""
    try:
        sum_func(1)
    except TypeError:
        pass

    captured = capsys.readouterr()
    assert "missing 1 required positional argument: 'y'" in captured.out





