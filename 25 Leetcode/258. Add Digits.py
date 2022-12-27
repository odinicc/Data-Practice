import math


def addDigits(num):
    check = 0
    while num > 9 or check == 0:
        n = list(str(num))
        n_i = [int(x) for x in n]
        num = int(sum(n_i))
        check = 1
    return num



num = 1232312

print(addDigits( num))


