# Модуль для считывания финансовых операций из CSV- и XLSX-файлов.

import logging
import os
from typing import List

import pandas as pd

###########
# Настройка логгера

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
os.makedirs("logs", exist_ok=True)

file_handler = logging.FileHandler("logs/file_processing.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)


def read_csv_operations(file_path: str) -> List:
    """Функция для считывания финансовых операция из CSV файла"""

    try:
        logger.debug(f"Чтение CSV-файла: {file_path}")
        # Проверка файла на существование и то что он не пустой
        if not os.path.exists(file_path):
            logger.warning(f"CSV-файл {file_path}не найден ")
            return []
        if os.path.getsize(file_path) == 0:
            logger.warning(f"CSV-файл {file_path} пуст ")
            return []
        # Чтение файла CSV c разделителем ";"
        df = pd.read_csv(file_path, sep=";")
        operations = df.to_dict(orient="records")

        # Замена NaN на None
        for operation in operations:
            for key, value in operation.items():
                if pd.isna(value):
                    operation[key] = None
        logger.info(f"Успешно загружено {len(operations)} транзакций из CSV")
        return operations

    # except Exception:
    #     #В случае любой ошибки возвращаем пустой список
    #     return []
    except pd.errors.EmptyDataError:
        logger.error(f"CSV-файл {file_path} пуст или содержит только заголовки ")
        return []
    except pd.errors.ParserError as exp:
        logger.error(f"Ошибка парсинга CSV-файла {file_path}: {exp}")
        return []
    except Exception as exp:
        logger.error(f"Ошибка при чтении CSV-файла {file_path}: {exp}")
        return []


def read_excel_operations(file_path: str) -> List:
    """Функция для чтения операций из Excel файла"""

    try:
        logger.debug(f"Чтение Excel-файла: {file_path}")
        if not os.path.exists(file_path):
            logger.warning(f"Excel-файл {file_path}не найден ")
            return []
        if os.path.getsize(file_path) == 0:
            logger.warning(f"Excel-файл {file_path} пуст")
            return []

        df = pd.read_excel(file_path)
        operations = df.to_dict(orient="records")
        for operation in operations:
            for key, value in operation.items():
                if pd.isna(value):
                    operation[key] = None
        logger.info(f"Успешно загружено {len(operations)} транзакций из Excel")
        return operations

    # except Exception:
    #     return []
    except ValueError as exp:
        logger.error(f"Ошибка чтения Excel-файла {file_path}: {exp}")
        return []
    except Exception as exp:
        logger.error(f"Ошибка при чтении Excel-файла {file_path}: {exp}")
        return []
