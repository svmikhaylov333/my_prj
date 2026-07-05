import json
import os
from typing import List


def load_operations(file_path: str) -> List:
    """
    Загружает транзакции из JSON-файла.
    """
    try:
        # Проверка что файл существует и он не пустой"
        if not os.path.exists(file_path):
            return []
        if os.path.getsize(file_path) == 0:
            return []

        # парисинг JSON Файла
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            # если JSON не список, возврат пустого спсика
            if not isinstance(data, list):
                return []
            return data

    except (json.JSONDecodeError, IOError, OSError):
        # В случае любой ошибки возвращаем пустой список
        return []
