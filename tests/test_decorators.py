from typing import Any, Dict, List

import pytest

from src.decorators import log
from src.masks import get_mask_card_number
from src.processing import filter_by_state, sort_by_date

# тест mask в консоль


def test_get_mask_card_number_success() -> None:
    @log()
    def test_get_mask_card_number(card_number: str) -> str:
        return get_mask_card_number(card_number)  # type: ignore[no-any-return]

    result: str = test_get_mask_card_number("1234567891234567")
    assert result == "1234 56** **** 4567"


# тест processing в файл


def test_filter_by_state_success(clean_log_file: str) -> None:
    """
    Тест filter_by_state успешно логирует в файл.
    """

    @log(clean_log_file)
    def test_log_filter_by_state_success(data: list[dict], state: str = "EXECUTED") -> list[dict]:
        return filter_by_state(data, state)  # type: ignore[no-any-return]

    test_data: List[Dict[str, Any]] = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
        {"id": 3, "state": "EXECUTED"},
    ]

    result: List[Dict[str, Any]] = test_log_filter_by_state_success(test_data, "EXECUTED")
    assert len(result) == 2

    with open(clean_log_file, "r", encoding="utf-8") as f:
        content: str = f.read()
        assert "test_log_filter_by_state_success -> ok" in content


def test_filter_by_state_error(clean_log_file: str) -> None:
    """
    Тест filter_by_state с ошибкой логирует в файл.
    """

    @log(clean_log_file)
    def test_log_filter_by_state_error(data: Any, state: str = "EXECUTED") -> Any:
        return filter_by_state(data, state)

    with pytest.raises(AttributeError):
        test_log_filter_by_state_error("not a list", "EXECUTED")

    with open(clean_log_file, "r", encoding="utf-8") as f:
        content: str = f.read()
        assert "test_log_filter_by_state_error" in content
        assert "not a list" in content
        assert "ERROR: AttributeError" in content


def test_sort_by_date_success(clean_log_file: str) -> None:
    """
    Тест sort_by_date успешно логирует в файл.

    """

    @log(clean_log_file)
    def test_log_sort_by_date_success(data: list[dict], reverse: bool = True) -> list[dict]:
        return sort_by_date(data, reverse)  # type: ignore[no-any-return]

    test_data: List[Dict[str, Any]] = [
        {"id": 1, "date": "2024-01-03"},
        {"id": 2, "date": "2024-01-01"},
        {"id": 3, "date": "2024-01-02"},
    ]

    result: List[Dict[str, Any]] = test_log_sort_by_date_success(test_data)
    assert result[0]["date"] == "2024-01-03"
    assert result[-1]["date"] == "2024-01-01"

    with open(clean_log_file, "r", encoding="utf-8") as f:
        content: str = f.read()
        assert "test_log_sort_by_date_success -> ok" in content


def test_sort_by_date_error(clean_log_file: str, capsys: Any) -> None:
    """
    проверка all_args = f"{args_str}, {kwargs_str}"

    """

    @log()
    def test_log_decorator_both_args_types(card_number: str, currency: str = "USD") -> str:
        return get_mask_card_number(card_number)  # type: ignore[no-any-return]

    result: str = test_log_decorator_both_args_types("1234567891234567", currency="USD")
    assert result == "1234 56** **** 4567"

    captured = capsys.readouterr()
    assert "test_log_decorator_both_args_types -> ok" in captured.out


def test_decorator_only_kwargs(capsys: Any) -> None:
    """
    проверка elif kwargs_str: all_args = kwargs_str

    """

    @log()
    def test_log_decorator_only_kwargs(data: Any = None, state: str = "EXECUTED") -> Any:
        if data is None:
            return []
        return filter_by_state(data, state)

    test_data: List[Dict[str, Any]] = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
    ]

    result: List[Dict[str, Any]] = test_log_decorator_only_kwargs(data=test_data, state="EXECUTED")
    assert len(result) == 1

    captured = capsys.readouterr()
    assert "test_log_decorator_only_kwargs -> ok" in captured.out


def test_decorator_no_args(capsys: Any) -> None:
    """
    проверка else: all_args = ""
    """

    @log()
    def test_log_decorator_no_args() -> str:
        return get_mask_card_number("1234567891234567")  # type: ignore[no-any-return]

    result: str = test_log_decorator_no_args()
    assert result == "1234 56** **** 4567"

    captured = capsys.readouterr()
    assert "test_log_decorator_no_args -> ok" in captured.out
