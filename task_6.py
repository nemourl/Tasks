import random

secret_num = random.randint(1, 100)
count = 0

print("Я загадал число от 1 до 100. Попробуй угадать!")

while True:
    number = input("Твой вариант: ")

    try:
        this_number = int(number)
    except ValueError:
        print("Ошибка! Введите целое число")
        continue

    if this_number < 1 or this_number > 100:
        print("Число должно быть в диапазоне от 1 до 100")
        continue 

    count += 1

    if this_number < secret_num:
        print("Загаданное число больше")
    elif this_number > secret_num:
        print("Загаданное число меньше")
    else:
        print(f"Поздравляю! Ты угадал число {secret_num} за {count} попытки!")
        break  # Выходим из цикла, игра окончена