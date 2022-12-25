import math

#def climbStairs(self, n):


def climbStairs(n):
    if n ==1:
        return 1
    if n ==2:
        return 2
    if n==3:
        return 3
    m = []
    m.append(1)
    m.append(2)
    m.append(3)

    for i in range(3,n):
        m.append(m[i-2]+m[i-1])
    return m[-1]

#5 - 8
#4 - 5


print(climbStairs(4))


