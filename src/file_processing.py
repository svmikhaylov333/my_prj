# Модуль для считывания финансовых операций из CSV- и XLSX-файлов.

import os
from typing import List
import pandas as pd



def read_csv_operations(file_path: str) -> List:
    """Функция для считывания финансовых операция из CSV файла"""

    try:
        # Проверка файла на существование и то что он не пустой
        if not os.path.exists(file_path):
            return []
        if os.path.getsize(file_path) == 0:
            return []
        #Чтение файла CSV c разделителем ";"
        df =pd.read_csv(file_path, sep=";")
        operations = df.to_dict(orient="records")

        # Замена NaN на None
        for operation in operations:
            for key, value in operation.items():
                if pd.isna(value):
                    operation[key] = None
        return operations

    except Exception:
        #В случае любой ошибки возвращаем пустой список
        return []


def read_excel_operations(file_path: str) -> List:
    """Функция для чтения рпераций из Excel файла"""

    try:
        if not os.path.exists(file_path):
            return []
        if os.path.getsize(file_path) == 0:
            return []

        df =pd.read_excel(file_path)
        operations =df.to_dict(orient="records")
        for operation in operations:
            for key, value in operation.items():
                if pd.isna(value):
                    operation[key]= None

        return operations
    except Exception:
        return []
