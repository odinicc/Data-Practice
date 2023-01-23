import re

def fairCandySwap(aliceSizes, bobSizes):
    a_s = sum(aliceSizes)
    b_s = sum(bobSizes)
    for a in aliceSizes:
        for b in bobSizes:
            if a_s - a + b == b_s - b+a:
                return [a,b]


aliceSizes = [1,3]
bobSizes = [2]
print(fairCandySwap(aliceSizes, bobSizes))

