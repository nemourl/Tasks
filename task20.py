lst1 = [1, 2, 3, 2, 4]
lst2 = [2,2,3,5]

common = []

temp_lst2 = lst2.copy()

for item in lst1:
    if item in temp_lst2:
        common.append(item)
        temp_lst2.remove(item)

common.sort(key=lambda x:lst1.index(x))
print(common)