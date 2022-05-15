import math
import sys

def read_data():
    #read from file
    inf = open("15.txt","r")

    #read from system input
    #inf = sys.stdin


    Lines  = inf.readlines()[1]
    List = list(Lines.split(" "))
    List = list(map(int, List))
    return List

def create_seq(A):
    D = []
    for i in range(len(A)):
        D.append(-1)

    for i in range(len(D)):
        D[i] = 1
        for j in range(0, i):
            Aj = A[j]
            Ai = A[i]
            Dj = D[j]
            Di = D[i]
            if A[j] < A[i] and D[j] + 1 > D[i]:
                D[i] = D[j] + 1
    return D

def create_elements(A,D):
    Overal = []
    length_of_long_ss = D.index(max(D))
    i = length_of_long_ss
    prev = i
    Overal.insert(0, A[i])
    while i >= 0:
        Ai = A[i]
        Di = D[i]
        Dprev = D[prev]
        if (A[i] < prev and D[i] == D[prev] - 1):
            Overal.insert(0, A[i])
            prev = i
        i -= 1
    return Overal

A = read_data()
D = create_seq(A)
Overal = create_elements(A,D)

print(*D)
print(*A)

print("Overal",Overal)





