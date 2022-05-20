import sys
from functools import lru_cache, partial
def read_data():
    # for local solution
    inf = open('19.txt', 'r')

    # for system solution
    # inf = sys.stdin

    Lines = inf.readline().replace('\n', '')
    Lines2 = inf.readline().replace('\n', '')
    A = list((Lines2.split(" ")))
    A = list(map(int, A))
    return A

@lru_cache()
def max_sum_stair(st):
    if len(A[st:]) == 1:
        return A[st]
    elif len(A[st:]) == 2:
        return max(A[st+1],A[st]+A[st+1])
    elif len(A) == 3:
        return max(A[st]+A[st+1]+A[st+2] ,A[st] +A[st+2] , A[st+1] +A[st+2])
    else:
        max_stair = max(A[st] + max_sum_stair(st+1), A[st+1] + max_sum_stair(st+2) )

    return max_stair

A = read_data()
#print(A[0:])
#print("--------")
B = max_sum_stair(0)
print(B)

