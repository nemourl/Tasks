num = int(input("Введите целое положительное число: "))

if num < 0:
    print("Ошибка: введите положительное число")
else:
    if num == 0:
        count = 1
        sum_digits = 0
        has_five = "Цифра 5 не найдена"
        is_palindrome = "да"
    else:
        original = num
        reversed_num = 0
        count = 0
        sum_digits = 0
        has_five = "Цифра 5 не найдена"
        
        while num > 0:
            digit = num % 10 
            
            count = count + 1
            
            sum_digits = sum_digits + digit
            
            if digit == 5:
                has_five = "Цифра 5 найдена"
            
            reversed_num = reversed_num * 10 + digit
            
            num = num // 10
        
        if original == reversed_num:
            is_palindrome = "да"
        else:
            is_palindrome = "нет"
    
    print("Количество цифр:", count)
    print("Сумма всех цифр:", sum_digits)
    print(has_five)
    print("Палиндром:", is_palindrome)