import math
from functools import reduce

def singleNumber(nums):
    out = 0
    for i in range(len(nums)):
        out_old= out
        out = out^nums[i]
        print (out_old, '^' ,nums[i],' => ',out  )
    return(out)

nums = [4,1,2,1,2]
print(singleNumber(nums))

