num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
operation = input("Введите операцию (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
    print("Результат:", result)
elif operation == "-":
    result = num1 - num2
    print("Результат:", result)
elif operation == "*":
    result = num1 * num2
    print("Результат:", result)
elif operation == "/":
    if num2 == 0:
        print("Ошибка: деление на ноль")
    else:
        result = num1 / num2
        print("Результат:", result)
else:
    print("Неизвестная операция")