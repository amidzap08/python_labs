def col_sums(mat: list[list[float | int]]) -> list[float]:
    if len(mat) == 0:
        return []
    first_row = len(mat[0])
    for row in mat:
        if len(row) != first_row:
            return "ValueError"
    sum_list = [0] * first_row
    for row in mat:
        for j in range(len(row)):
            sum_list[j] = sum_list[j] + row[j]
    return sum_list


print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
