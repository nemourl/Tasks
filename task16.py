lst = [1, 2, 3, 4, 5]
lst_res = lst.copy()
for i in range(0, len(lst_res) - 1, 2):
    lst_res[i], lst_res[i + 1] = lst_res[i + 1], lst_res[i]
print(lst_res)