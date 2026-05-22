original = {
    "Анна": "Python",
    "Борис": "Java",
    "Вера": "Python",
    "Глеб": "C++",
    "Диана": "Java"
}

inverted = {}

for name, language in original.items():
    inverted.setdefault(language, []).append(name)
print(inverted)