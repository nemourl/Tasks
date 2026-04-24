lst = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5]
compressed = []
count = 1

for i in range(1, len(lst)):
    if lst[i] == lst[i-1]:
        count += 1
    else:
        if count == 1:
            compressed.append(lst[i-1])
        else:
            compressed.append([lst[i-1], count])
        count = 1

if count == 1:
    compressed.append(lst[-1])
else:
    compressed.append([lst[-1], count])

print(compressed)

