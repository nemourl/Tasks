students = {
    "Анна": [5, 4, 5, 4],
    "Борис": [3, 3, 4, 5],
    "Вера": [5, 5, 5, 4]
}

average_grades = {
    name: sum(grades) / len(grades)
    for name, grades in students.items()
}

print(average_grades)