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
    A = [0] + A
    return A


def max_sum_stair(A):
    N = len(A)
    cum = 0
    B = [None]*N
    B[0] = 0
    B[1] = A[1]
    for i in range(2,N):
        B[i] = max(B[i-1],B[i-2])+A[i]

    return B[-1]



A = read_data()
#print("A[:7]" , A[:7])
#print("--------")
B = max_sum_stair(A)
print(B)

