def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    max = -100000000
    min = 100000000
    if len(nums) == 0:
        return "ValueError"
    for i in range(len(nums)):
        if nums[i] > max:
            max = nums[i]
    for j in range(len(nums)):
        if nums[j] < min:
            min = nums[j]
    return (min, max)


print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([]))
print(min_max([1.5, 2, 2.0, -3.1]))
