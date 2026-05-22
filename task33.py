data = [
    ("фрукты", "яблоки", 10),
    ("фрукты", "груши", 5),
    ("овощи", "морковь", 7),
    ("фрукты", "яблоки", 12),
    ("овощи", "свекла", 4)
]

nested = {}

for category, subcategory, value in data:
    nested.setdefault(category, {})[subcategory] = value

print(nested)