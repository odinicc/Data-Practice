import math

#def generate(self, numRows):
def majorityElement(nums):
    max_elem = None
    cnt = 0
    for i in nums:
        if cnt == 0:
            max_elem = i
        if i == max_elem:
            cnt += 1
        else:
            cnt -= 1
        print(max_elem,' -- ',cnt)

    return max_elem


nums = [1,1,1,1,3,3,2,2]
print(majorityElement(nums))

