import math

def getMinDistance(nums, target, start):
    t = []
    for i in range(len(nums)):
        if nums[i] == target:
            t.append(i)
    t = [abs(start-x) for x in t]
    return min(t)



nums = [1,1,1,1,1,1,1,1,1,1]
target = 1
start = 0


print(getMinDistance(nums, target, start))


#%%
