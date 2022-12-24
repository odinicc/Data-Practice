import math

def isPowerOfThree(n):
    poww = math.log(n,3)
    if poww.is_integer():
        return True
    else:
        return False

print(isPowerOfThree(9))

