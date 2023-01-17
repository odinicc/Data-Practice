import math

#def twoSum(self, nums, target):
def twoSum(nums, target):
    nums = [int(x) for x in nums]
    target = int(target)
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                print(nums[i] , nums[j])
                return [i,j]



nums = [3,3]
target = 6
print(twoSum(nums,target))


