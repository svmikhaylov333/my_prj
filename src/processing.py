import re
from src.decorators import log


@log("logs/processing.log")
def filter_by_state(list_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state"""
    return [item for item in list_dict if item.get("state") == state]


@log("logs/processing.log")
def sort_by_date(list_dict: list[dict], reverse: bool = True) -> list[dict]:
    """Функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате (date)."""
    return sorted(list_dict, key=lambda x: x["date"], reverse=reverse)


def process_bank_search(data:list[dict], search:str)->list[dict]:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска,
    возвращает список словарей у которых в описании есть данная строка"""

    if not data or not search:
        return []

    result =[]
    for operation in data:
        description =operation.get("description", "")
        if re.search(re.escape(search), description, re.I):
            result.append(operation)
    return result

def process_bank_operations(data:list[dict], categories:list)->dict:
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций
    в каждой категории. Категории операций хранятся в поле description."""

    if not data or not categories:
        return {category: 0 for category in categories} if categories else {}
    result ={category:0 for category in categories}

    for operation in data:
        description =operation.get("description", "")
        for category in categories:
           if category.lower() in description.lower():
                result[category] += 1

    return result