import math

def isUgly(n):
    if n == 0 or n == 1:
        return True
    if n < 0:
        return False
    i = abs(n)
    while i > 1:
        if i%2 == 0:
            i =i/2
        elif i%3 == 0:
            i =i/3
        elif i%5 == 0:
            i = i/5
        else:
            return False
    return True

def isUgly2( n):
    for p in 2, 3, 5:
        while n % p == 0 < n:
            n /= p
    return n == 1


n = -2147483648

print(isUgly(n))
print(isUgly2(n))


#%%
