def flatten(mat: list[list | tuple]) -> list:
    result = []
    for row in mat:
        if (type(row)!=list and type(row)!=tuple):
            return "TypeError"
        for j in row:
            result.append(j)
    return result

print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))
