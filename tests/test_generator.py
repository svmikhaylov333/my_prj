import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

# тест filter_by_currency


def test_filter_by_currency_usd(transactions: list[dict]) -> None:
    """тест - фильтрация по USD."""
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 3
    for t in result:
        assert t["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_no_match(transactions: list[dict]) -> None:
    """тест - валюты нет —>  пустой список."""
    result = list(filter_by_currency(transactions, "EUR"))
    assert len(result) == 0


def test_filter_by_currency_empty_list(empty_transactions: list[dict]) -> None:
    """тест - обработка пустого списка."""
    result = list(filter_by_currency(empty_transactions, "USD"))
    assert len(result) == 0


def test_filter_by_currency_malformed(
    malformed_transactions: list[dict],
) -> None:
    """тест - обработку некорректных данных."""
    result = list(filter_by_currency(malformed_transactions, "USD"))
    assert len(result) == 0


# тест transaction_descriptions


def test_transaction_descriptions(transactions: list[dict]) -> None:
    """тест - получение описаний транзакций."""
    result = list(transaction_descriptions(transactions))
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    assert result == expected


def test_transaction_descriptions_empty(
    empty_transactions: list[dict],
) -> None:
    """тест -обработка пустого списка."""
    result = list(transaction_descriptions(empty_transactions))
    assert len(result) == 0


def test_transaction_descriptions_attribute_error() -> None:
    """
    Тест transaction_descriptions с AttributeError
    """


transactions = [
    {"description": "Есть описание"},
    "not a dict",
    123,
    {"description": "Еще одно описание"},
    None,
]

result = list(transaction_descriptions(transactions))
expected = ["Есть описание", "Еще одно описание"]
assert result == expected


def test_transaction_descriptions_missing() -> None:
    """тест -  отсутствия описания возвращается стандартное сообщение."""
    transactions: list[dict] = [
        {"description": "Есть описание"},
        {"id": 123},
    ]
    result = list(transaction_descriptions(transactions))
    assert result == ["Есть описание", "Описания нет"]


# тест card_number_generator


def test_card_number_generator_small() -> None:
    """тест - генерацию номеров в небольшом диапазоне."""
    result = list(card_number_generator(1, 5))
    expected = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]
    assert result == expected


def test_card_number_generator_format() -> None:
    """тест - проверка форматирования номеров карт."""
    result = list(card_number_generator(1234567891234567, 1234567891234569))
    expected = [
        "1234 5678 9123 4567",
        "1234 5678 9123 4568",
        "1234 5678 9123 4569",
    ]
    assert result == expected


def test_card_number_generator_single() -> None:
    """тест - проверка генерацию одного номера."""
    result = list(card_number_generator(1, 1))
    assert result == ["0000 0000 0000 0001"]


def test_card_number_generator_stop() -> None:
    """тест- генератор правильно завершается."""
    gen = card_number_generator(1, 3)
    assert next(gen) == "0000 0000 0000 0001"
    assert next(gen) == "0000 0000 0000 0002"
    assert next(gen) == "0000 0000 0000 0003"
    with pytest.raises(StopIteration):
        next(gen)
