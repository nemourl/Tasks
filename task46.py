import re


def cont_digit(string):
    pattern = r'\d'
    return bool(re.search(pattern, string))


print(cont_digit("abc1def"))  # True
print(cont_digit("abcdef"))   # False