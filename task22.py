matrix = [[1, 2, 3], [4, 5, 6]]

transposed = []
for j in range(len(matrix[0])):
    row = []
    for i in range(len(matrix)):
        row.append(matrix[i][j])
    transposed.append(row)

print(transposed)