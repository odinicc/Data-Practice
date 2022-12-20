

import math
import sys
from collections import deque

def read_data():
    #read from file
    inf = open("05 Create Binary Heap.txt","r")

    #read from system input
    #inf = sys.stdin

    lines = inf.readlines()

    lis = lines[1].rstrip('\n')

    inf.close()
    lis = lis.split()
    lis = list(map(int, lis))

    return lis


def max_elems(lis,k):
    Dq = deque()
    n = len(lis)
    overal =[]
    #create initial deque
    for i in range(k):
        if len(Dq) == 0:
            Dq.append(i)
        else:
            if lis[i] > lis[Dq[-1]]:
                Dq.pop()
                Dq.append(i)
            else:
                Dq.append(i)
    for i in range(k,n):
        overal.append(lis[Dq[0]])
        # Remove the elements which are
        # out of this window
        while Dq and Dq[0] <= i - k:
            # remove from front of deque
            Dq.popleft()
        while Dq and lis[i] >= lis[Dq[-1]]:
            Dq.pop()
        Dq.append(i)
    overal.append(lis[Dq[0]])

    return overal


lis = read_data()
print(lis)









