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


def max_sum_stair(A):
    #print(A)
    if len(A) == 1:
        return A[0]
    elif len(A) == 2:
        return max(A[1],A[0]+A[1])
    elif len(A) == 3:
        return max(A[0]+A[1]+A[2] ,A[0] +A[2] , A[1] +A[2])
    else:
        max_stair = max(A[0] + max_sum_stair(A[1:]), A[1] + max_sum_stair(A[2:]) )

    return max_stair

A = read_data()
#print(A[2:])
#print("--------")
B = max_sum_stair(A)
print(B)

