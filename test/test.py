from src.masks import get_mask_card_number, get_mask_account

print(get_mask_card_number("1234 5678 9123 456q"))
print(get_mask_card_number("1234 5678 9123 456"))

print(get_mask_card_number("1234 5678 9123 4567"))
print(get_mask_account("123"))
print(get_mask_account("1234 5678 9123 4567"))