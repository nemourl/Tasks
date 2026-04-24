lst = [1, 2, 2, 3, 2, 4, 1]
unique_lst = []
for item in lst:
    if item not in unique_lst:
        unique_lst.append(item)
print(unique_lst)
