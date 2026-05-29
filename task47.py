import re


def find_words(text):
    pattern = r'\b[A-Z][a-zA-Z]*\b'
    return re.findall(pattern, text)

text = "Hello, World! This is a Test."

print(find_words(text))