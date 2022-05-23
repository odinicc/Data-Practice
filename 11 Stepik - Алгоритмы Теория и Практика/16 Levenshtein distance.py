import math
import sys
from pandas import *

def read_data():
    #read from file
    inf = open("16.txt","r")

    #read from system input
    #inf = sys.stdin

    Lines  = inf.readline().replace('\n', '')
    A = list(Lines)
    Lines2 = inf.readline().replace('\n', '')
    B = list(Lines2)
    return A ,B

def diff(a,b):
    if a==b:
        return 0
    else:
        return 1

def levenshtein_matrix(A,B):
    w = len(A) + 1
    h = len(B) + 1
    # print("w = ",w,"h = ",h)
    D = [[None for x in range(w)] for y in range(h)]
    D[0][0] = 0

    for i in range(1, h):
        D[i][0] = D[i - 1][0] + 1

    for j in range(1, w):
        D[0][j] = D[0][j - 1] + 1

    for i in range(1, h):
        for j in range(1, w):
            c = diff(A[j - 1], B[i - 1])
            # print(A_code[j-1],B[i-1],c,"|D[i-1][j]", D[i-1][j],"|D[i][j-1]", D[i][j-1])
            one = D[i - 1][j] + 1
            two = D[i][j - 1] + 1
            three = D[i - 1][j - 1] + c
            # print(one, two, three)
            D[i][j] = min(one, two, three)
    return D , h, w

A, B = read_data()
#print(A_code)
#print(B)
D , h, w = levenshtein_matrix(A,B)
print(DataFrame(D))
#print(D[y][x])
#print(D[7][5])
#print(D[i][j])
# h = 8, w = 6
print(D[h-1][w-1])