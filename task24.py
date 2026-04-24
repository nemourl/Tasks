table = [
    ["B", 100, 4.5],
    ["A", 100, 4.5],
    ["C", 50, 5.0],
    ["D", 100, 5.0],
]

sorted_table = sorted(table, key=lambda row: (row[1], -row[2], row[0]))

print(sorted_table)