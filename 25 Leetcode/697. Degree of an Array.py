import math
import string

def max_sublen(nums,elem):
    for i in range(len(nums)):
        if nums[i] == elem:
            min_e = i
            break
    for i in range(len(nums)-1,-1,-1):
        if nums[i] == elem:
            max_e = i
            break
    return max_e - min_e+1



def findShortestSubArray(nums):
    d = {}

    for i in range(len(nums)):
        if nums[i] not in d:
            d[nums[i]] = 1
        else:
            d[nums[i]] += 1
    min_len = len(nums)

    max_len = 1
    for k in d.keys():
        if d[k] > max_len:
            max_len = d[k]

    for k in d.keys():
        if d[k] == max_len:

            min_len_new = max_sublen(nums,k)
            #print(k,' - ',d[k],' - ', min_len_new)
            if min_len_new < min_len:
                min_len = min_len_new

    return min_len



    #elem= max(set(nums), key=nums.count)
    #print(max_sublen(nums,elem))


nums = [1,2,2,3,1,4,2]
print(max_sublen(nums,2))
print(findShortestSubArray(nums))

for index, num in enumerate(nums):
    print(index, num)


