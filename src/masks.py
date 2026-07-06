import logging
import os

# настройка логгера для модуля masks
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# создание папки, если ее нет
os.makedirs("logs", exist_ok=True)

# настройка handler
file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
# настройка Formatter
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты - XXXX XX** **** XXXX"""
    try:
        card_number = str(card_number).replace(" ", "")
        if len(card_number) != 16 or not card_number.isdigit():
            logger.error(f"Неверный номер карты: {card_number}")
            return "Неверный номер карты"
        logger.info(f"Номер карты {card_number[-4:]} замаскирован")
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    except Exception as exp:
        logger.error(f"Ошибка при маскировке номера карты: {exp}")
        return "Неверный номер карты"


def get_mask_account(account: str) -> str:
    """Маскирует номер банковского счета - **XXXX"""
    try:
        account = str(account).replace(" ", "")
        if len(account) < 4 or not account.isdigit():
            logger.error(f"Неверный номер счета: {account}")
            return "Неверный номер счета"
        result = f"**{account[-4:]}"
        logger.info(f"Успешно замаскирован номер счета: {result}")
        return result
    except Exception as exp:
        logger.error(f"Ошибка при маскировке номера счета: {exp}")
        return "Неверный номер счета"
