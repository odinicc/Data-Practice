import math

#def longestCommonPrefix(self, strs):
def canPlaceFlowers(flowerbed, n):
    if flowerbed[0] == 0:
        flowerbed.insert(0,0)
    if flowerbed[-1] == 0:
        flowerbed.append(0)
    for i in range(len(flowerbed)-2):
        if flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i+2] == 0:
            flowerbed[i+1] = 1
            n -= 1
        if n == 0:
            break
    if n == 0:
        return True
    else:
        return False




flowerbed = [0,0,1,0,1]
n = 1
print(canPlaceFlowers(flowerbed, n))


