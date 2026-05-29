import re


def find_emails(text):
    pattern = r'\b\w+@\w+\.\w+\b'
    return re.findall(pattern, text)

text = "Contact us: support@hello.com or admin@site.org."

print(find_emails(text))