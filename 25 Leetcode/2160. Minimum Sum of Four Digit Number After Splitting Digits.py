import math


def minimumSum(num):
    n = list(str(num))
    n = [int(x) for x in n]

    n.sort()
    n1 = str(n[0]) + str(n[2])
    n2 = str(n[1]) + str(n[3])
    return int(n1) + int(n2)

num = 2932

print(minimumSum(num))



