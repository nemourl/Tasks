import re


def normal_spaces(text):
    pattern = r'\s+'
    return re.sub(pattern, ' ', text)


text = "This is \t a\n test."

print(normal_spaces(text))