import json
import logging
import os
from typing import List

# настройка логгера для модуля utils
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# создание папки, если ее нет
os.makedirs("logs", exist_ok=True)

# настройка handler
file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
# настройка Formatter
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def load_operations(file_path: str) -> List:
    """
    Загружает транзакции из JSON-файла.
    """
    try:
        logger.debug(f"Попытка загрузки файла: {file_path}")
        # Проверка что файл существует и он не пустой"
        if not os.path.exists(file_path):
            logger.warning(f"Файл не найден: {file_path}")
            return []
        if os.path.getsize(file_path) == 0:
            logger.warning(f"Файл пустой: {file_path}")
            return []

        # парсинг JSON Файла
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            # если JSON не список, возврат пустого списка
            if not isinstance(data, list):
                logger.error(f"Данные в файле {file_path} не являются списком")
                return []
            logger.info(f"Успешно загружено {len(data)} транзакций из {file_path}")
            return data

    except Exception as exp:
        # В случае любой ошибки возвращаем пустой список
        logger.error(f"ошибка при загрузке файла {file_path}: {exp}")
        return []
