lst1 = [1, 3, 5]
lst2 = [2, 4, 6, 7]

merged = []
i, j = 0, 0
m = len(lst1)
n = len(lst2)

while i < m or j < n:
    if j == n or (i < m and lst1[i] <= lst2[j]):
        merged.append(lst1[i])
        i += 1
    else:
        merged.append(lst2[j])
        j += 1

print(merged)