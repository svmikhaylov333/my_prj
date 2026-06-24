from typing import Any, Dict, Iterator, List


def filter_by_currency(transactions: list[dict], currency: str = "USD") -> Iterator[dict]:
    """
       принимает на вход список словарей, представляющих транзакции.
    Функция возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (по умолчанию, USD).
    """
    for transaction in transactions:
        try:
            if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
                yield transaction
        except AttributeError:
            continue


def transaction_descriptions(
    transactions: List[Dict[str, Any]],
) -> Iterator[str]:
    """
    Генератор, возвращающий описания транзакций по очереди.
    """
    for transaction in transactions:
        try:
            yield transaction.get("description", "Описания нет")
        except AttributeError:
            continue


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    генератор - выдает номера банковских карт в формате
    XXXX XXXX XXXX XXXX, где X  — цифра номера карты.
    """
    for number in range(start, end + 1):
        formatted = f"{number:016d}"
        yield (f"{formatted[:4]} {formatted[4:8]} " f"{formatted[8:12]} {formatted[12:16]}")
