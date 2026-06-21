import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card_or_account_info, exp",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        (
            "Visa Platinum 8990922113665229",
            "Visa Platinum 8990 92** **** 5229",
        ),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счеafhbaehafh54108430135874305", "Введены неверные данные"),
        ("Счеaf r r ", "Введены неверные данные"),
        ("Счеaf 736 ", "Введены неверные данные"),
    ],
)
def test_mask_account_card(card_or_account_info: str, exp: str) -> None:
    """тест маскировки информации о карте или счете"""
    assert mask_account_card(card_or_account_info) == exp


@pytest.mark.parametrize(
    "date, exp",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024 03 11T02:26:18.671407", "Неверный формат даты"),
        ("1234 5678 9123 4567", "Неверный формат даты"),
        ("123", "Неверный формат даты"),
    ],
)
def test_get_date(date: str, exp: str) -> None:
    """Тест смены формата даты 2024-03-11T02:26:18.671407 в
    "ДД.ММ.ГГГГ" ("11.03.2024")"""
    assert get_date(date) == exp
