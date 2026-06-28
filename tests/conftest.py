import pytest
import os


@pytest.fixture
def test_data_processing() -> list[dict]:
    """Общая фикстура для тестов processing.py"""
    return [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
        },
        {
            "id": 615064591,
            "state": "CANCELED",
            "date": "2018-10-14T08:21:33.419441",
        },
        {
            "id": 888064591,
            "state": "CANCELED",
            "date": "2026-06-14T08:21:33.419441",
        },
        {
            "id": 888064591,
            "date": "2026-06-14T08:21:33.419441",
        },
        {
            "id": 888064591,
            "state": "HJGJJH",
            "date": "2026-06-14T08:21:33.419441",
        },
    ]


# Фикструты для generators
@pytest.fixture
def transactions() -> list[dict]:
    """Фикстура с примерами транзакций для тестов."""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def empty_transactions() -> list[dict]:
    """Фикстура с пустым списком транзакций."""
    return []


@pytest.fixture
def malformed_transactions() -> list[dict]:
    """Фикстура с транзакциями, у которых неправильная структура."""
    return [
        {"operationAmount": "не словарь"},
        {"operationAmount": {"currency": "не словарь"}},
        {"id": 123},
        {},
    ]


@pytest.fixture
def clean_log_file():
    """
    Фикстура: создает директорию для логов.

    """
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_dir = os.path.join(project_root, "tests", "logs")
    log_file = os.path.join(log_dir, "log.txt")

    os.makedirs(log_dir, exist_ok=True)

    yield log_file