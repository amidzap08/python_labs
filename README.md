# Лабораторная работа №2
## python
## Задание 1(1)
```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    max = -100000000
    min = 100000000
    if (len(nums) == 0):
        return "ValueError"
    for i in range(len(nums)):
        if nums[i] > max:
            max = nums[i]
    for j in range(len(nums)):
        if nums[j] < min:
            min = nums[j]
    return (min, max)
```
![Выявление минимума и максимума](/src/lab02/images/01.arrays.png)

## Задание 1(2)
```python
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    nums1 = set(nums)
    nums2 = sorted(nums1)
    return nums2
```  
![ Вернуть отсортированный список уникальных значений по возрастанию](/src/lab02/images/02.arrays.png)
## Задание 1(3)
```python
def flatten(mat: list[list | tuple]) -> list:
    result = []
    for row in mat:
        if (type(row)!=list and type(row)!=tuple):
            return "TypeError"
        for j in row:
            result.append(j)
    return result
```
![«Расплющить» кортежи в один список по строкам](/src/lab02/images/03.arrays.png)

## Задание 2(1)
```python
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
```
![Поменять строки и столбцы местами](/src/lab02/images/01.matrix.png)

## Задание 2(2)
```python
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
```
![Вычисление суммы каждой строки матрицы](/src/lab02/images/02.matrix.png)
## Задание 2(3)
```python
def col_sums(mat: list[list[float | int]]) -> list[float]:
    if (len(mat)==0):
        return []
    first_row = len(mat[0])
    for row in mat:
        if (len(row)!=first_row):
            return "ValueError"
    sum_list = [0]*first_row
    for row in mat:
        for j in range(len(row)):
            sum_list[j] = sum_list[j]+row[j] 
    return sum_list
```
![Вычисление суммы каждого столбца матрицы](/src/lab02/images/03.matrix.png)

## Задание 3(1)
```python
def format_record(rec: tuple[str, str, float]) -> str:

    if not isinstance(rec, tuple):                    
        raise TypeError
    
    if len(rec) != 3:
        raise ValueError
    
    fio, group, gpa = rec

    if not isinstance(fio, str) or not isinstance(group, str):  
        raise TypeError
    
    if not isinstance(gpa, float):
        raise TypeError

    if not fio:                                            
        raise ValueError
    if not group:
        raise ValueError
    
    if not gpa:
        raise ValueError
    
    parts = fio.strip().split()                      
    if len(parts) < 2:
        raise ValueError
    surname = parts[0].title()                                     
    initials = "".join(p[0].upper() + '.' for p in parts[1:])       

    group = group.strip()

    gpa = f"{float(gpa):.2f}"
    return f"{surname} {initials}, гр. {group}, GPA {gpa}"


```
![Работа с "записями" как с кортежами](/src/lab02/images/01.tuples.png)






