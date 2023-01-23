import math
import string

def dominantIndex(nums):
    m_max = max(nums)
    for n in nums:
        if n != 0:
            if n != m_max and m_max/n < 2:
                return -1
    return nums.index(m_max)

nums = [1,2,3,4]
print(dominantIndex(nums))


