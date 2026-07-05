from src.decorators import log
from src.masks import get_mask_account, get_mask_card_number

# def get_mask_card_number(card_number: str) -> str:
#     """Маскирует номер банковской карты - XXXX XX** **** XXXX"""
#
#     card_number = str(card_number).replace(" ", "")
#     if len(card_number) != 16 or not card_number.isdigit():
#         return "Неверный номер карты"
#     return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
#
#
# def get_mask_account(account: str) -> str:
#     """Маскирует номер банковского счета - **XXXX"""
#
#     account = str(account).replace(" ", "")
#     if len(account) < 4 or not account.isdigit():
#         return "Неверный номер счета"
#     return f"**{account[-4:]}"
#


@log("logs/widget.log")
def mask_account_card(card_or_account_info: str) -> str:
    """Маскирует информацию о карте или счете
    Примеры:
    "Visa Platinum 7000792289606361" -> "Visa Platinum 7000 79** **** 6361"
    "Счет 73654108430135874305" -> "Счет **4305"
    """

    parts = card_or_account_info.rsplit(" ", 1)

    if len(parts) != 2:
        return "Введены неверные данные"

    type_card_or_account = parts[0]
    number = parts[1]

    if not number.isdigit():
        return "Введены неверные данные"

    if "Счет" in type_card_or_account:
        return f"{type_card_or_account} {get_mask_account(number)}"
    else:
        return f"{type_card_or_account} {get_mask_card_number(number)}"


@log("logs/widget.log")
def get_date(date: str) -> str:
    """меняет формат даты 2024-03-11T02:26:18.671407 в
    "ДД.ММ.ГГГГ" ("11.03.2024")"""
    if len(date) < 10:
        return "Неверный формат даты"
    date_part = date[:10]
    if "-" not in date_part:
        return "Неверный формат даты"
    # parts = date_part.split("-")
    # if len(parts) !=3:
    #     return "Введены неверные данные"
    # else:
    #     return f"{parts[2]}.{parts[1]}.{parts[0]}"
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"
