import math

def findGCD(nums):
    n_min = min(nums)
    n_max = max(nums)
    print(n_min,'--',n_max)
    n = min(n_min,n_max)
    for i in range(n,0,-1):
        if n_min%i == 0 and n_max%i == 0:
            return i



nums = [3,9]


print(findGCD(nums))

