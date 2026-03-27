count = 0
vowels = "аеёиоуыэюя"

text = input("Введите строку: ")
text.lower()

for char in text:
    if char in vowels:
        count += 1

print("Количество гласных: ", count)



