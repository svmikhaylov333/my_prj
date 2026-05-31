from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

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

test_list_dict = [
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
    },
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
    },
    {
        "id": 615064591,
        "state": "CANCELED",
        "date": "2018-10-14T08:21:33.419441",
    },
]

print("=" * 50)
print("проверка filter_by_state")
print("=" * 50)
print(filter_by_state(test_list_dict, "EXECUTED"))

print("=" * 50)
print("проверка sort_by_date")
print("=" * 50)
print(sort_by_date(test_list_dict))
print(sort_by_date(test_list_dict, False))
