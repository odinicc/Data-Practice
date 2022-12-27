import math

def summaryRanges(nums):
    if len(nums) == 0:
        return ''


    my_l = [[nums[0]]]
    prev = nums[0]
    for i in range(1,len(nums)):
        if nums[i]-prev == 1:
            my_l[-1].append(nums[i])
        else:
            my_l.append([nums[i]])
        prev = nums[i]
    res = []
    for elem in my_l:
        first = str(elem[0])
        last = str(elem[-1])
        if first == last:
            res.append(first)
        else:
            res.append(first + '->' + last)
    return res


nums = [0,2,3,4,6,8,9]


print(summaryRanges(nums))


#%%
