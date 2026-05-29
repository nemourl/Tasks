import re
from datetime import datetime


def find_dates(text):
    pattern = r'\b\d{2}\.\d{2}\.\d{4}\b'

    dates = re.findall(pattern, text)

    valid_dates = []

    for date in dates:
        try:
            datetime.strptime(date, "%d.%m.%Y")
            valid_dates.append(date)
        except ValueError:
            pass

    return valid_dates

text = """
Оплатить до 31.02.2023 или 28.02.2023.
Дедлайн 29.02.2024.
"""

print(find_dates(text))