"""
Strong Password Detection
Write a function that uses regular expressions to make sure the password
string it is passed is strong.
A strong password is deﬁned as one that is at least eight characters
long, contains both uppercase and lowercase characters, and has at least
one digit.
You may need to test the string against multiple regex patterns to
validate its strength.
"""

import re

eight_char_re = re.compile(r'[a-zA-Z0-9]{8,}')
upper_re = re.compile(r'[A-Z]+')
lower_re = re.compile(r'[a-z]+')
one_digit_re = re.compile(r'\d+')

def check_pwd_strength(password):
    """Checks if the provided password is a strong one."""
    if eight_char_re.search(password):
        if upper_re.search(password):
            if lower_re.search(password):
                if one_digit_re.search(password):
                    return True
    return False

password_list = [
    'password',
    'password123',
    '123456',
    'PaSSWoRD',
    'Password123',
]

for passwd in password_list:
    if check_pwd_strength(passwd):
        print(f"'{passwd}' is a strong password.")
    else:
        print(f"'{passwd}' is too weak!")
        