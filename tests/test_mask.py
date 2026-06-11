import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, exp",
    [
        ("1234567891234567", "1234 56** **** 4567"),
        ("1234 5678 9123 4567", "1234 56** **** 4567"),
        ("1234-5678-9123-4567", "Неверный номер карты"),
        ("1234 5678 9123 456q", "Неверный номер карты"),
        ("1234 5678 9123 456", "Неверный номер карты"),
        ("1234 5678 9123 456123", "Неверный номер карты"),
    ],
)
def test_get_mask_card_number(card_number: str, exp: str) -> None:
    """Тест маскировки номера банковской карты - XXXX XX** **** XXXX"""
    assert get_mask_card_number(card_number) == exp


@pytest.mark.parametrize(
    "account, exp",
    [
        ("1234567891234567", "**4567"),
        ("91234567", "**4567"),
        ("dsssgs", "Неверный номер счета"),
        ("i234567891234567", "Неверный номер счета"),
    ],
)
def test_get_mask_account(account: str, exp: str) -> None:
    """Тест маскировки номер банковского счета - **XXXX"""
    assert get_mask_account(account) == exp
