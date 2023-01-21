import math

def smallerNumbersThanCurrent(nums):
    nums2 = nums.copy()
    nums2.sort()
    print(nums2, nums)
    res = []
    for n in nums:
        for ni2 in range(len(nums)):
            print(n, ' -- ', ni2 ,nums2[ni2])
            if nums2[ni2] == n:
                res.append(ni2)
                break

    return res

nums = [8,1,2,2,3]
print(smallerNumbersThanCurrent(nums))

#%%
