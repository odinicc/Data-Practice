import math
import sys

def read_data():
    #read from file
    inf = open("14.txt","r")

    #read from system input
    #inf = sys.stdin


    Lines  = inf.readlines()[1]
    List = list(Lines.split(" "))
    List = list(map(int, List))
    return List

A = read_data()
print(len(A))
D = []
for i in range(len(A)):
    D.append(-1)
#D[0] = 1
print(*D)

for i in range(len(D)):
    D[i] = 1
    print(type(A[i]))
    if A[i] == 8:
        print("hi")
    for j in range(0,i):
        Aj = A[j]
        Ai = A[i]
        Dj = D[j]
        Di = D[i]
        if A[j] < A[i] and D[j]+1 > D[i]:
            D[i] = D[j]+1

print(*A)
print(*D)

Overal = []
length_of_long_ss = D.index(max(D))
print(A[length_of_long_ss])

i = length_of_long_ss
prev = i
Overal.insert(0,A[i])
while i >= 0:
    Ai = A[i]
    Di = D[i]
    Dprev = D[prev]
    if (A[i] < prev and D[i] == D[prev]-1):

        Overal.insert(0,A[i])
        prev = i
    i -= 1

print("Overal",Overal)





