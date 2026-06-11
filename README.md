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
- Poetry
- Flake8
- Black
- Isort
- Mypy
- Pytest

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
python tests/test.py
```
или

```bash
pytest
```
для проверки покрытия проверки

```bash
pytest --cov
```

сформировать отчет, см. htmlcov/index.html
 ```bash
pytest --cov=src --cov-report=html
```

Проверяются:

- маскирование карт;
- маскирование счетов;
- форматирование дат;
- обработка строк с реквизитами;
- фильтрация операций;
- сортировка операций.

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
- [ ] ...


---

## Команда проекта

MC

---
## Источники

---
