import math


def findPoisonedDuration(timeSeries, duration):
    out = 0
    n= len(timeSeries)
    if n == 0: return 0
    for i in range(n-1):
        out += min(timeSeries[i+1] - timeSeries[i], duration)
    return out + duration


timeSeries = [1,2,5,6,7,8]
print(timeSeries[::2])
duration = 2
print(findPoisonedDuration(timeSeries, duration))
#print(Increasing(nums))