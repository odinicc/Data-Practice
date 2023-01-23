import math


#def lengthOfLastWord(self, s):
def maximumProduct(nums):
    if len(nums) == 3:
        return nums[0]*nums[1]*nums[2]
    else:
        p = []
        max_1 = max(nums)
        p.append(max_1)
        nums.remove(max_1)
        max_2 = max(nums)
        p.append(max_2)
        nums.remove(max_2)
        max_3 = max(nums)
        p.append(max_3)
        nums.remove(max_3)
        if len(nums) > 0:
            min_1 = min(nums)
            p.append(min_1)
            nums.remove(min_1)
        if len(nums) > 0:
            min_2 = min(nums)
            p.append(min_2)
            nums.remove(min_2)
        if len(nums) > 0:
            min_3 = min(nums)
            p.append(min_3)
            nums.remove(min_3)
    m_max = 1
    for i in range(len(p)):
        for j in range(len(p)):
            for k in range(len(p)):
                if i != j and j != k and i != k:
                    if p[i]*p[j]*p[k] > m_max:
                        m_max = p[i]*p[j]*p[k]
    return m_max



nums = [1,2,3,4,4,5,10]
print(maximumProduct(nums))


