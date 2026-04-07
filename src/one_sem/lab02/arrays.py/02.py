def unique_sorted(nums: list[float | int]) -> list[float | int]:
    nums1 = set(nums)
    nums2 = sorted(nums1)
    return nums2


print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))
