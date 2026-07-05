from src.decorators import log


@log("logs/masks.log")
def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты - XXXX XX** **** XXXX"""

    card_number = str(card_number).replace(" ", "")
    if len(card_number) != 16 or not card_number.isdigit():
        return "Неверный номер карты"
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


@log("logs/masks.log")
def get_mask_account(account: str) -> str:
    """Маскирует номер банковского счета - **XXXX"""

    account = str(account).replace(" ", "")
    if len(account) < 4 or not account.isdigit():
        return "Неверный номер счета"
    return f"**{account[-4:]}"
