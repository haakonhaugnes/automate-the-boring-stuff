#! python3
# strongPasswordDetection.py - a program to test password strength

import re

import re


def is_strong_password(password):
    """Checks whether a password is strong using a single regular expression."""

    pattern = r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$'

    if re.search(pattern, password):
        return True
    else:
        return False


# Test the function with some sample passwords
passwords = ['password123', 'PaSsWoRd', 'p@ssword', 'P4s$w0rd']

for password in passwords:
    if is_strong_password(password):
        print(f"{password} is a strong password")
    else:
        print(f"{password} is not a strong password")
