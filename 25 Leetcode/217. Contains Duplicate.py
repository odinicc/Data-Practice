import math

def containsDuplicate(nums):

    my_l = []
    for i in range(len(nums)):
        if nums[i] in my_l:
            return True
        else:
            my_l.append(nums[i])

    return False


nums = [1,23,2,5]
print(containsDuplicate(nums))

