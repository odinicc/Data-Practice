import math

#def mySqrt(self, x):
def mySqrt(x):
    start = 1
    end = x
    while start*start != x and end*end != x:
        mid = (start+end) // 2
        mid2 = mid*mid
        if mid2 > x:
            end = mid
        elif mid2 < x:
            start = mid
        else:
            return mid
    return mid




print(mySqrt(16))


