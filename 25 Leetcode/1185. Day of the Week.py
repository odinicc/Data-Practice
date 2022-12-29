import math

def moveZeroes(nums):
    stack = []
    i = 0
    while i < len(nums):
        print(nums , i)
        if nums[i] == 0:
            nums.pop(i)
            stack.append(0)
        else:
            i += 1

    return nums + stack
nums = [0,0,1]

print(moveZeroes(nums))

