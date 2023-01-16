import math

def merge(nums1, m, nums2, n):
    result =[]
    iter1 = 0
    iter2 = 0
    while iter1 < m and iter2 < n:
        if nums1[iter1] < nums2[iter2]:
            result.append(nums1[iter1])
            iter1 += 1
        else:
            result.append(nums2[iter2])
            iter2 += 1

    if iter1 == m and iter2 != n:
        result += nums2[iter2:n]
    elif iter1 != m and iter2 == n:
        result += nums1[iter1:m]

    return result




nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3
print(merge(nums1,m,nums2,n))


