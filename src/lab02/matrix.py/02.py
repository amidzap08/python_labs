def row_sums(mat: list[list[float | int]]) -> list[float]:
    result = []
    for row1 in mat:
        if (len(row1)!=len(mat[0])):
            return "ValueError"
    for row in mat:
        sum = 0
        for i in row:
            sum = sum + i
        result.append(sum)
    return result

print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))