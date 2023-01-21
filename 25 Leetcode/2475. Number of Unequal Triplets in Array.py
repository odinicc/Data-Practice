import math
import re
from collections import Counter

def unequalTriplets(nums):
    c = Counter(nums)
    #print(c)
    #print(c.keys())
    res = 0

    m = list(c.keys())
    for i1 in range(len(m) - 2 ):
        for i2 in range(i1+1,len(m) - 1):
            for i3 in range(i2+1,len(m)):
                #print(m[i1],' - ',m[i2],' - ',m[i3])
                res += c[m[i1]]*c[m[i2]]*c[m[i3]]

    return res

nums = [1,3,1,2,4]
print(unequalTriplets(nums))

