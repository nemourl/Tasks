import re


def is_int(string):
    pattern = r'^[+-]?\d+$'
    return bool(re.fullmatch(pattern, string))


print(is_int("123"))    # True
print(is_int("-007"))   # True
print(is_int("12.3"))   # False
print(is_int("+"))      # False