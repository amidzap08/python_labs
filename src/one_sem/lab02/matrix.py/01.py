def transpose(mat: list[list[float | int]]) -> list[list]:
    if len(mat) == 0:
        return []

    first_row_len = len(mat[0])
    for i in range(1, len(mat)):
        if len(mat[i]) != first_row_len:
            return ValueError

    res = []
    for j in range(len(mat[0])):
        new_row = []
        for i in range(len(mat)):
            new_row.append(mat[i][j])
        res.append(new_row)
    return res


print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))
