import math


#def plusOne(self, digits):
def removeDuplicates(nums):
    prev = -101
    for i in range(len(nums)):
        if nums[i] == prev:
            nums[i] = 101
        else:
            prev = nums[i]

    nums.sort()
    print(nums)
    if 101 in nums:
        return nums.index(101)
    else:
        return len(nums)


def removeDuplicates2(A):
    if not A:
        return 0

    newTail = 0

    for i in range(1, len(A)):
        if A[i] != A[newTail]:
            newTail += 1
            A[newTail] = A[i]

    print(  nums)
    return newTail + 1


nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates2(nums))

