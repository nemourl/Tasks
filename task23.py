nested_list = [1, [2, 3], [[4], [5, 6]], 7]

flat_list = []
temp = [nested_list]

while temp:
    item = temp.pop(0)
    if type(item) == list:
        for x in item[::-1]:
            temp.insert(0, x)
    else:
        flat_list.append(item)

print(flat_list) 