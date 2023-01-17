from statistics import mode

#def twoSum(self, nums, target):
def twoSum(nums, target):
    n = len(nums)
    a = sum(nums)
    b = sum(set(nums))

    s = n*(n+1)//2
    print(b)
    print(a-b)
    print(s-b)


nums = [1,2,2,4]
target = 6
print(twoSum(nums,target))


