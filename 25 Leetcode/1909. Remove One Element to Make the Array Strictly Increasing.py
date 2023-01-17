import math

def Increasing(nums):
    for i in range(1,len(nums)):
        if nums[i] < nums[i-1]:
            return False
    return True


def canBeIncreasing(nums):
    if len(nums) == 2:
        return True
    else:
        for i in range(1,len(nums)):
            if nums[i-1] > nums[i]:
                if Increasing(nums[:i] + nums[i + 1:]) or Increasing(nums[:i-1] + nums[i :]) :
                    return True
                else:
                    return False
    return True





nums = [1,2,10,5,7]
print(canBeIncreasing(nums))
#print(Increasing(nums))