capacity = 3
actions = [1, 2, 3, 4, 5]

buffer = []

for num in actions:
    if len(buffer) < capacity:
        buffer.append(num)
    else:
        buffer.pop(0)
        buffer.append(num)
    print(buffer)