students = {
    "Анна": True,
    "Борис": False,
    "Вера": True,
    "Диана": False
}

all_names = ["Анна", "Борис", "Вера", "Глеб", "Диана", "Елена"]

absent = []
failed = []

for name in all_names:
    check = students.get(name)

    if check is None:
        absent.append(name)
    elif check is False:
        failed.append(name)

print("Отсутствует", absent)
print("Не сдали:", failed)