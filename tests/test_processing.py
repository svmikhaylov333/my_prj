import os
import tempfile
from unittest.mock import MagicMock, patch

import pandas as pd

from src.file_processing import read_csv_operations, read_excel_operations
from src.processing import process_bank_search, process_bank_operations

# Тесты CSV


def test_read_csv_operations_success() -> None:
    """Тест чтения CSV-файла"""
    # создание тестовых данных
    test_data = pd.DataFrame(
        [{"id": 1, "amount": 100.5, "currency": "USD"}, {"id": 2, "amount": 200.0, "currency": "EUR"}]
    )

    # создание временного CSV-файл
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False, encoding="utf-8") as tmp_file:
        test_data.to_csv(tmp_file.name, sep=";", index=False)
        tmp_file_path = tmp_file.name

    try:
        result = read_csv_operations(tmp_file_path)
        assert len(result) == 2
        assert result[0]["id"] == 1
        assert result[0]["amount"] == 100.5
        assert result[0]["currency"] == "USD"
    finally:
        os.unlink(tmp_file_path)


def test_read_csv_operations_not_found() -> None:
    """Тест при отсутствии CSV-файла"""
    result = read_csv_operations("non_existent_file.csv")
    assert result == []


def test_read_csv_operations_empty_file() -> None:
    """Тест при пустом CSV-файле"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False, encoding="utf-8") as tmp_file:
        tmp_file_path = tmp_file.name

    try:
        result = read_csv_operations(tmp_file_path)
        assert result == []
    finally:
        os.unlink(tmp_file_path)


def test_read_csv_operations_only_headers() -> None:
    """Тест CSV-файла при отсутсвии данных"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False, encoding="utf-8") as tmp_file:
        tmp_file.write("id;amount;currency\n")
        tmp_file_path = tmp_file.name

    try:
        result = read_csv_operations(tmp_file_path)
        assert result == []
    finally:
        os.unlink(tmp_file_path)


def test_read_csv_operations_with_nan() -> None:
    """Тест CSV-файла с пустыми значениями"""
    test_data = pd.DataFrame(
        [
            {"id": 1, "amount": 100.5, "currency": "USD", "from": None},
            {"id": 2, "amount": 200.0, "currency": "EUR", "from": "Visa 1234"},
        ]
    )

    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False, encoding="utf-8") as tmp_file:
        test_data.to_csv(tmp_file.name, sep=";", index=False)
        tmp_file_path = tmp_file.name

    try:
        result = read_csv_operations(tmp_file_path)
        assert len(result) == 2

        assert result[0]["from"] is None
        assert result[1]["from"] == "Visa 1234"
    finally:
        os.unlink(tmp_file_path)


@patch("src.file_processing.pd.read_csv")
def test_read_csv_operations_parser_error(mock_read_csv: MagicMock) -> None:
    """Тест при ошибке парсинга CSV"""
    mock_read_csv.side_effect = pd.errors.ParserError("Parse error")

    # создание временного файла
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False, encoding="utf-8") as tmp_file:
        tmp_file.write("id;amount\n1;100")
        tmp_file_path = tmp_file.name

    try:
        result = read_csv_operations(tmp_file_path)
        assert result == []
    finally:
        os.unlink(tmp_file_path)


@patch("src.file_processing.pd.read_csv")
def test_read_csv_operations_empty_data_error(mock_read_csv: MagicMock) -> None:
    """Тест - ошибка EmptyDataError"""
    mock_read_csv.side_effect = pd.errors.EmptyDataError("Empty data")

    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False, encoding="utf-8") as tmp_file:
        tmp_file_path = tmp_file.name

    try:
        result = read_csv_operations(tmp_file_path)
        assert result == []
    finally:
        os.unlink(tmp_file_path)


# Тесты для EXCEL


@patch("src.file_processing.pd.read_excel")
def test_read_excel_operations_success(mock_read_excel: MagicMock) -> None:
    """Тест чтения Excel-файла"""

    mock_df = pd.DataFrame(
        [{"id": 1, "amount": 100.5, "currency": "USD"}, {"id": 2, "amount": 200.0, "currency": "EUR"}]
    )
    mock_read_excel.return_value = mock_df

    # Создание временного файла)
    with tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False) as tmp_file:
        tmp_file_path = tmp_file.name

    try:
        # записывается test, чтобы файл был не пустым
        with open(tmp_file_path, "w") as f:
            f.write("test")

        result = read_excel_operations(tmp_file_path)
        assert len(result) == 2
        assert result[0]["id"] == 1
        assert result[0]["amount"] == 100.5
    finally:
        os.unlink(tmp_file_path)


def test_read_excel_operations_not_found() -> None:
    """Тест при отсутствии Excel-файла"""
    result = read_excel_operations("non_existent_file.xlsx")
    assert result == []


def test_read_excel_operations_empty_file() -> None:
    """Тест при пустом Excel-файле"""
    with tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False) as tmp_file:
        tmp_file_path = tmp_file.name

    try:
        result = read_excel_operations(tmp_file_path)
        assert result == []
    finally:
        os.unlink(tmp_file_path)


@patch("src.file_processing.pd.read_excel")
def test_read_excel_operations_value_error(mock_read_excel: MagicMock) -> None:
    """Тест ошибка ValueError"""
    mock_read_excel.side_effect = ValueError("Excel format error")

    with tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False) as tmp_file:
        tmp_file_path = tmp_file.name
        with open(tmp_file_path, "w") as f:
            f.write("test")

    try:
        result = read_excel_operations(tmp_file_path)
        assert result == []
    finally:
        os.unlink(tmp_file_path)


@patch("src.file_processing.pd.read_excel")
def test_read_excel_operations_general_error(mock_read_excel: MagicMock) -> None:
    """Тест ошибка чтения Excel"""
    mock_read_excel.side_effect = Exception("General error")

    with tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False) as tmp_file:
        tmp_file_path = tmp_file.name
        with open(tmp_file_path, "w") as f:
            f.write("test")

    try:
        result = read_excel_operations(tmp_file_path)
        assert result == []
    finally:
        os.unlink(tmp_file_path)


@patch("src.file_processing.pd.read_excel")
def test_read_excel_operations_with_nan(mock_read_excel: MagicMock) -> None:
    """Тест Excel-файла с пустыми значениями"""
    mock_df = pd.DataFrame(
        [
            {"id": 1, "amount": 100.5, "currency": "USD", "from": None},
            {"id": 2, "amount": 200.0, "currency": "EUR", "from": "Visa 1234"},
        ]
    )
    mock_read_excel.return_value = mock_df

    with tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False) as tmp_file:
        tmp_file_path = tmp_file.name
        with open(tmp_file_path, "w") as f:
            f.write("test")

    try:
        result = read_excel_operations(tmp_file_path)
        assert len(result) == 2
        assert result[0]["from"] is None
        assert result[1]["from"] == "Visa 1234"
    finally:
        os.unlink(tmp_file_path)


def test_process_bank_search_found() -> None:
    """Тест поиска - найдено совпадение"""
    data = [
        {"description": "Перевод организации", "amount": 100},
        {"description": "Открытие вклада", "amount": 200},
    ]
    result = process_bank_search(data, "Перевод")
    assert len(result) == 1
    assert result[0]["description"] == "Перевод организации"


def test_process_bank_search_not_found() -> None:
    """Тест поиска - ничего не найдено"""
    data = [{"description": "Перевод организации", "amount": 100}]
    result = process_bank_search(data, "Карта")
    assert result == []


def test_process_bank_search_empty_data() -> None:
    """Тест с пустым списком или пустой строкой"""

    result = process_bank_search([], "Перевод")
    assert result == []


    data = [{"description": "Перевод организации", "amount": 100}]
    result = process_bank_search(data, "")
    assert result == []


def test_process_bank_search_case_insensitive() -> None:
    """Тест поиска - игнорируемый регистр"""
    data = [
        {"description": "Перевод организации", "amount": 100},
        {"description": "перевод с карты", "amount": 200},
    ]
    result = process_bank_search(data, "перевод")
    assert len(result) == 2


def test_process_bank_operations_success() -> None:
    """Тест подсчета категорий"""
    data = [
        {"description": "Перевод организации", "amount": 100},
        {"description": "Перевод организации", "amount": 200},
        {"description": "Открытие вклада", "amount": 300},
    ]
    categories = ["Перевод организации", "Открытие вклада"]

    result = process_bank_operations(data, categories)
    assert result["Перевод организации"] == 2
    assert result["Открытие вклада"] == 1


def test_process_bank_operations_empty() -> None:
    """Тест с пустыми данными"""
    categories = ["Перевод организации", "Открытие вклада"]
    result = process_bank_operations([], categories)
    assert result["Перевод организации"] == 0
    assert result["Открытие вклада"] == 0

    data = [{"description": "Перевод организации", "amount": 100}]
    result = process_bank_operations(data, [])
    assert result == {}