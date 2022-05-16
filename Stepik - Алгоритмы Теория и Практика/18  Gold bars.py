import random
import sys
from pandas import *

def read_data():
    # for local solution
    inf = open('18.txt', 'r')

    # for system solution
    # inf = sys.stdin

    Lines = inf.readline().replace('\n', '')
    A = list(Lines.split(" "))
    back_pack = int(A[0])
    n = int(A[1])
    Lines2 = inf.readline().replace('\n', '')
    B = list(Lines2.split(" "))
    goods = []
    for i in range(len(B)):
        elem = [int(B[i]),int(B[i])]
        goods.append(elem)
    return goods, n ,back_pack


def crate_matrix(goods, n ,back_pack):
    D = []
    for x in range(n + 1):
        M = []
        for y in range(back_pack + 1):
            M = M + [0]
        D = D +[M]
    # D[y][x] | D[i][w]

    for i in range(1, n + 1):
        for w in range(1, back_pack + 1):
            D[i][w] = D[i - 1][w]
            wi = goods[i - 1][1]
            if wi <= w:
                Ci = goods[i - 1][0]
                Dwi = D[i][w]
                Dwi_1 = D[i - 1][w - wi]
                D[i][w] = max(Dwi, Dwi_1 + Ci)

    return D

def determine_goods(goods,n,back_pack,D):
    overal = [None for x in range(n)]
    w = back_pack
    overal_price = D[n][back_pack]
    for i in range(n, 0, -1):
        #print("Cycle  i=", i, "|w=", w, "|D[i][w]", D[i][w])
        if D[i][w] == D[i - 1][w]:
            overal[i - 1] = 0
        else:
            overal[i - 1] = 1
            overal_price = overal_price - goods[i - 1][0]
            for g in range(w, 0, -1):
                if D[i - 1][g] == overal_price:
                    break
            w = g
    return overal

goods, n ,back_pack = read_data()
#print("goods", goods)
#print(DataFrame(goods))
#print("n", n)
#print("back_pack", back_pack)
D = crate_matrix(goods, n ,back_pack)
print(D[n][back_pack])
print(DataFrame(D))
#overal = determine_goods(goods,n,back_pack,D)

#print(overal)