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
    return  B, n, back_pack


B, n, back_pack = read_data()
print("n = ", n)
print("back_pack = ", back_pack)
print("B = ", B)



#print("goods", goods)
#print(DataFrame(goods))



#overal = determine_goods(goods,n,back_pack,D)

#print(overal)