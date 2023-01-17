import math

def findErrorNums(nums):
    nums.sort()
    for i in range(len(nums)):
        if i+1 not in nums:
            missing_val = i+1
    #nums.append(missing_val)
    #nums.sort()
    for i in range(len(nums)):
        if nums[i]> missing_val:
            nums.insert(i,missing_val)
            break
    print(nums)
    for i in range(len(nums)):
        if i+1 != nums[i]:
            additional_val = nums[i]
            break
    m = [additional_val,missing_val]

    return m




nums = [2,2]
print(findErrorNums(nums))



#%%
