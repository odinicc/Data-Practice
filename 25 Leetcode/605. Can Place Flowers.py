import math

#def longestCommonPrefix(self, strs):
def nextGreaterElement(nums1, nums2):
    res = []
    nums2
    for n in nums1:
        i = nums2.index(n)
        if i == len(nums2)-1:
            res.append(-1)
        else:
            res.append(nums2[i+1])
    return res




nums1 = [4,1,2]
nums2 = [1,3,4,2]

print(nextGreaterElement(nums1, nums2))


