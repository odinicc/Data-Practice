import math


def missingNumber(nums):
    l = len(nums)
    nums = set(nums)
    for i in range(l):
        if i not in nums:
            return int(i)

nums = [0,2]

print(missingNumber(nums))


