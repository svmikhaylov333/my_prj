import json
import os
import tempfile
from unittest.mock import mock_open, patch

import pytest

from src.utils import load_operations


def test_load_operations_success() -> None:
    """Тест успешной загрузки транзакций"""
    test_data = [{"id": 1, "amount": 100, "currency": "USD"}, {"id": 2, "amount": 200, "currency": "EUR"}]

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as tmp_file:
        json.dump(test_data, tmp_file)
        tmp_file_path = tmp_file.name

    try:
        result = load_operations(tmp_file_path)
        assert result == test_data
    finally:
        os.unlink(tmp_file_path)


def test_load_operations_empty_file() -> None:
    """Тест пустого файла - возвращает пустой список"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as tmp_file:
        tmp_file_path = tmp_file.name

    try:
        result = load_operations(tmp_file_path)
        assert result == []
    finally:
        os.unlink(tmp_file_path)


def test_load_operations_not_found() -> None:
    """Тест отсутствующего файла - возвращает пустой список"""
    result = load_operations("non_existent_file.json")
    assert result == []


def test_load_operations_invalid_json() -> None:
    """Тест некорректного JSON - возвращает пустой список"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as tmp_file:
        tmp_file.write("{invalid json}")
        tmp_file_path = tmp_file.name

    try:
        result = load_operations(tmp_file_path)
        assert result == []
    finally:
        os.unlink(tmp_file_path)


def test_load_operations_not_list() -> None:
    """Тест когда JSON не список - возвращает пустой список"""
    test_data = {"id": 1, "amount": 100}

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as tmp_file:
        json.dump(test_data, tmp_file)
        tmp_file_path = tmp_file.name

    try:
        result = load_operations(tmp_file_path)
        assert result == []
    finally:
        os.unlink(tmp_file_path)
