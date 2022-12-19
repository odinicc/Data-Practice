

import math
import sys
from collections import deque

def read_data():
    #read from file
    inf = open("04 Max in floating window.txt","r")

    #read from system input
    #inf = sys.stdin

    lines = inf.readlines()

    lis = lines[1].rstrip('\n')
    k  =  lines[2].rstrip('\n')

    inf.close()
    lis = lis.split()
    list(map(int, lis))
    k = int(k)
    print( 'type(lis[2])', type(lis[2]))
    return lis, k


def max_elems(lis,k):
    Dq = deque()
    n = len(lis)
    #create initial deque
    for i in range(k):
        print('lis[i] ',  lis[i])
        print('Dq ', Dq)
        if len(Dq) == 0:
            Dq.append(i)
            print('Dq 2 - ', Dq)
        else:
            if lis[i] > lis[Dq[-1]]:
                Dq.pop()
                Dq.append(lis[i])

    print(Dq)
    return  0


lis,k = read_data()
print('k ',k)
print('lis ',lis)
print(max_elems(lis,k))









