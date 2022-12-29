import math
import itertools


#def twoSum(self, nums, target):
def sumOddLengthSubarrays(arr):
    def len_sum(arr,n):
        m = 0
        for i in range(len(arr)-n+1):
            m += sum(arr[i:i+n])
        return m

    def isood(n):
        if n % 2 == 0:
            return False
        else:
            return True

    l = len(arr)
    prime_stack = []
    for i in range(1,l+1):
        if isood(i):
            prime_stack.append(i)
    m = 0
    for j in prime_stack:
        m += len_sum(arr,j)
    return m




arr = [6,9,14,5,3,8,7,12,13,1]
print('m = ',sumOddLengthSubarrays(arr))
