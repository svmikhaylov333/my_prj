# Banking_widget

![Python Version](https://img.shields.io/badge/python-3.9+-blue)
![Status](https://img.shields.io/badge/status-development-blue)
![Style](https://img.shields.io/badge/code%20style-black-blue)
![Version](https://img.shields.io/badge/version-0.0.1-blue)

Виджет, который показывает несколько последних успешных банковских операций.
Проект позволяет маскировать номера банковских карт и счетов, 
форматировать дату операций, фильтровать и сортировать банковские операции.

---

## Содержание

- [Технологии](#технологии)
- [Установка](#установка)
- [Использование](#использование)
- [Разработка](#разработка)
- [Тестирование](#тестирование)
- [Deploy и CI/CD](#deploy-и-cicd)
- [Contributing](#contributing)
- [FAQ](#faq)
- [To do](#to-do)

---

## Технологии

- Python 3.12
- Poetry - управление зависимостями и виртуальным окружением
- Flake8 - линтер для проверки стиля кода (PEP 8
- Black -  автоматическое форматирование кода
- Isort - сортировка импортов
- Mypy - проверка типов
- Pytest -тестирование кода
- pandas - для работы с CSV и Excel
- openpyxl - для чтения Excel-файлов
- requests - для API-запросов
- python-dotenv - для работы с .env
---

## Установка

```bash
git clone <repository-url>
cd my_prj
poetry install
poetry shell
```

---

## Использование

### Маскирование номера карты

```python
from src.masks import get_mask_card_number

print(get_mask_card_number("1234567891234567"))
# 1234 56** **** 4567
```

### Маскирование номера счета

```python
from src.masks import get_mask_account

print(get_mask_account("12345678901234567890"))
# **7890
```

### Маскирование карты или счета

```python
from src.widget import mask_account_card

print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))
```

### Форматирование даты

```python
from src.widget import get_date

print(get_date("2024-03-11T02:26:18.671407"))
# 11.03.2024
```

### Фильтрация операций

```python
from src.processing import filter_by_state

test_list_dict = [
    {"id": 41428829,"state": "EXECUTED", "date": "2019-07-03T18:35:29.512364",},
    {"id": 939719570,"state": "EXECUTED","CANCELED": "2018-06-30T02:08:58.425572",},
    ]

result = filter_by_state(test_list_dict)
```

### Сортировка операций

```python
from src.processing import sort_by_date

test_list_dict = [
    {"id": 41428829,"state": "EXECUTED", "date": "2019-07-03T18:35:29.512364",},
    {"id": 939719570,"state": "EXECUTED","CANCELED": "2018-06-30T02:08:58.425572",},
    ]

result = sort_by_date(test_list_dict)
```
### Генерация данных по транзакциям

```python
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

# Фильтрация транзакций по валюте
transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"}
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
   
]

# Получить все USD-транзакции
usd_transactions = list(filter_by_currency(transactions, "USD"))

# Получить описания всех транзакций
descriptions = list(transaction_descriptions(transactions))

# Сгенерировать номера карт в диапазоне
cards = list(card_number_generator(1, 5))
# Результат: ["0000 0000 0000 0001", "0000 0000 0000 0002", ...]
```
### Чтение данных из CSV

```python
from src.file_processing import read_csv_operations

# Чтение транзакций из CSV-файла
transactions = read_csv_operations("data/transactions.csv")
print(f"Загружено {len(transactions)} транзакций")
```
### Чтение данных из Excel

```python
from src.file_processing import read_excel_operations

# Чтение транзакций из Excel-файла
transactions = read_excel_operations("data/transactions_excel.xlsx")
print(f"Загружено {len(transactions)} транзакций")
```
### Загрузка данных из JSON
```python
from src.external_api import convert_currency

# Конвертация суммы транзакции в рубли
transaction = {"amount": 100, "currency": "USD"}
amount_in_rub = convert_currency(transaction)
print(f"Сумма в рублях: {amount_in_rub}")  # 7550.0
```
### Конвертация валют
```python
from src.external_api import convert_currency

# Конвертация суммы транзакции в рубли
transaction = {"amount": 100, "currency": "USD"}
amount_in_rub = convert_currency(transaction)
print(f"Сумма в рублях: {amount_in_rub}")  # 7550.0
```

---

## Разработка

### Требования

- Python 3.12+
- Poetry

### Проверка качества кода

```bash
flake8 .
black .
isort .
mypy .
```

---

## Тестирование

Для запуска проверки функций:

```bash
pytest
```
доп. проверки
```bash
python tests/test.py
```
для анализа покрытия кода тестами использовать

```bash
pytest --cov
```

сформировать отчет, см. htmlcov/index.html
 ```bash
pytest --cov=src --cov-report=html
```
сформировать отчет "без .gitignore", см. htmlcov/index.html
 ```bash
pytest --cov=src --cov-report=html; Remove-Item htmlcov/.gitignore
```
Если папка (не пустая) htmlcov  существует  и в ней удален .gitignore. 
при повторных генерациях .gitignore не создается

Проверяются:

- маскирование карт;
- маскирование счетов;
- форматирование дат;
- обработка строк с реквизитами;
- фильтрация операций;
- сортировка операций;
- конвертация валют;
- чтение CSV и Excel файлов.


---

## Deploy и CI/CD

На текущем этапе CI/CD отсутствует.

## Contributing

По вопросам и предложениям писать на почту.

---
## FAQ

Ответы на вопросы..

---
### Для чего нужен проект?

тренировочный проект

---

## To do

- [x] Маскирование карт
- [x] Маскирование счетов
- [x] Форматирование дат
- [x] Фильтрация операций
- [x] Сортировка операций
- [x] Генераторы для работы с транзакциями
- [x] Чтение CSV-файлов
- [x] Чтение Excel-файлов
- [x] Конвертация валют
- [x] Логирование
- [ ] ...


---

## Команда проекта

MC

---
## Источники

---
