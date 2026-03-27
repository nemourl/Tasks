N = int(input("Введите верхнюю границу N: "))

for i in range(2, N + 1):
    is_prime = True
    for num in range(2, i):
        if i % num == 0:
            is_prime = False
            break
    if is_prime:
        print(i, end=" ")

