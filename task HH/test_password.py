"""
Программа проверки корректности пароля
"""

password = "erer"
password_set = set(password)
all_digit_set = set('0123456789')

if not all_digit_set & password_set:
    print("Password must contain at least one digit")