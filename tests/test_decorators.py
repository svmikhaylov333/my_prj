import pytest

from src.decorators import log
from src.masks import get_mask_card_number
from src.processing import filter_by_state, sort_by_date


# тест mask в консоль

def test_get_mask_card_number_success() -> None:
    @log()
    def test_get_mask_card_number(card_number):
        return get_mask_card_number(card_number)

    result = test_get_mask_card_number("1234567891234567")
    assert result == "1234 56** **** 4567"

#тест proccessing в файл

def test_filter_by_state_success(clean_log_file) -> None:
    """
    Тест filter_by_state успешно логирует в файл.
    """

    @log(clean_log_file)
    def test_log_filter_by_state_success(data, state="EXECUTED"):
        return filter_by_state(data, state)

    test_data = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
        {"id": 3, "state": "EXECUTED"},
    ]

    result = test_log_filter_by_state_success(test_data, "EXECUTED")
    assert len(result) == 2

    with open(clean_log_file, "r", encoding="utf-8") as f:
        content = f.read()
        assert "test_log_filter_by_state_success -> ok" in content


def test_filter_by_state_error(clean_log_file) -> None:
    """
    Тест filter_by_state с ошибкой логирует в файл.
    """
    @log(clean_log_file)
    def test_log_filter_by_state_error(data, state="EXECUTED"):
        return filter_by_state(data, state)

    with pytest.raises(AttributeError):
        test_log_filter_by_state_error("not a list", "EXECUTED")

    with open(clean_log_file, "r", encoding="utf-8") as f:
        content = f.read()
        assert "test_func" in content
        assert "not a list" in content
        assert "ERROR: AttributeError" in content


def test_sort_by_date_success(clean_log_file) -> None:
    """
    Тест sort_by_date успешно логирует в файл.

    """
    @log(clean_log_file)
    def test_log_sort_by_date_success(data, reverse=True):
        return sort_by_date(data, reverse)

    test_data = [
        {"id": 1, "date": "2024-01-03"},
        {"id": 2, "date": "2024-01-01"},
        {"id": 3, "date": "2024-01-02"},
    ]

    result = test_log_sort_by_date_success(test_data)
    assert result[0]["date"] == "2024-01-03"
    assert result[-1]["date"] == "2024-01-01"

    with open(clean_log_file, "r", encoding="utf-8") as f:
        content = f.read()
        assert "test_func -> ok" in content

