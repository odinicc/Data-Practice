import math

#def climbStairs(self, n):


def minCostClimbingStairs(cost):
    res = [None]*(len(cost))
    pek = [None]*(len(cost))
    res[0] = cost[0]
    pek[0] = 1
    res[1] = min(cost[0],cost[1])
    if res[1] == cost[1]:
        pek[1] = 1
    else:
        pek[1] = 0
        res[1] = cost[0]
    if len(cost) > 2:
        if cost[0] + cost[2] < cost[1]:
            res[2] = cost[0] + cost[2]
            pek[2] = 1
        else:
            res[2] = cost[1]
            pek[2] = 0

    #print(res)
    #print(pek)
    if len(cost) >= 3:
        for i in range(3,len(cost)):
            if pek[i-1] == 1:
                a1 = res[i-1]
            else:
                a1 = res[i-1] + cost[i]
            if pek[i-2] == 1:
                a2 = res[i-2]+min(cost[i],cost[i-1])
            else:
                a2 = res[i-2] + cost[i-1]
            if a1 < a2:
                res[i] = a1
                if pek[i-1] == 1:
                    pek[i] = 0
                else:
                    pek[i] = 1
            else:
                res[i] = a2
                if pek[i-2] == 1:
                    if cost[i] < cost[i-1]:
                        pek[i] = 1
                    else:
                        pek[i] = 0
                else:
                    pek[i] = 0
        #print(res)
        #print(pek)
    return res[-1]

def minCostClimbingStairs2(cost):
    for i in range(len(cost) - 3, -1, -1):
        cost[i] += min(cost[i+1], cost[i+2])
    return min(cost[0], cost[1])


cost = [10,15]


print(minCostClimbingStairs(cost))


