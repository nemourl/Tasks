words = ["Анна", "арбуз", "Борис", "бинокль", "Вера", "арфа", "Белка"]

groups = {}

for word in words:
    f_letter = word[0].lower()
    groups.setdefault(f_letter, []).append(word)

print(groups)