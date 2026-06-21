def filter_by_state(list_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state"""
    return [item for item in list_dict if item.get("state") == state]


def sort_by_date(list_dict: list[dict], reverse: bool = True) -> list[dict]:
    """Функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате (date)."""
    return sorted(list_dict, key=lambda x: x["date"], reverse=reverse)
