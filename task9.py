grades = {
    (90, 100): "A (Отлично)",
    (75, 89): "B (Хорошо)",
    (60, 74): "С (Удовлетворительно)",
    (50, 59): "D (Неудовлетворительно)",
    (0, 49): "F (Провал)",
}

while True:
    score = int(input("Введите процент выполнения теста (от 0 до 100): "))

    if 0 <= score <= 100:
        for (min, max), grade in grades.items():
            if min <= score <= max:
                print(grade)
                break

        break
    else:
        print("Введите число от 0 до 100")