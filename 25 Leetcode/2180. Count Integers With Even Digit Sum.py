import math


def countEven(num):
    checker = 0
    for i in range(1,num+1):
        if digit_sum_is_even(i) == True:
            checker += 1
    return checker

def digit_sum_is_even(num):
    n = list(str(num))
    n = [int(x) for x in n]
    m = sum(n)
    if m % 2 ==0:
        return True
    else:
        return False

print(countEven(4))