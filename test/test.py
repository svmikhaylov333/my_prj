from src.masks import get_mask_card_number, get_mask_account
from src.widget import  mask_account_card, get_date

print("=" * 50)
print("проверка get_mask_card_number")
print("=" * 50)

print(get_mask_card_number("1234 5678 9123 456q"))
print(get_mask_card_number("1234 5678 9123 456"))
print(get_mask_card_number("1234 5678 9123 4567"))

print("=" * 50)
print("проверка get_mask_account")
print("=" * 50)

print(get_mask_account("123"))
print(get_mask_account("1234 5678 9123 4567"))

print("=" * 50)
print("проверка get_date")
print("=" * 50)

print(get_date("1234 5678 9123 4567"))
print(get_date("2024-03-11T02:26:18.671407"))

print("=" * 50)
print("проверка mask_account_card")
print("=" * 50)

test_data = [
    "Maestro 1596837868705199",
    "Счет 64686473678894779589",
    "MasterCard 7158300734726758",
    "Счет 35383033474447895560",
    "Visa Classic 6831982476737658",
    "Visa Platinum 8990922113665229",
    "Visa Gold 5999414228426353",
    "Счет 73654108430135874305",
    "Счеafhbaehafh54108430135874305",
    "Счеaf r r ",
]

for item in test_data:
    result = mask_account_card(item)
    print(f"{item:<35} -> {result}")
    # print(f"{item} -> {result}")