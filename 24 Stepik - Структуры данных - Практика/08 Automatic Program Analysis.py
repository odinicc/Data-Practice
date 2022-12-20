

import sys
import math

swapper = []

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



def swap(lis,a,b):
    lis[b], lis[a]= lis[a], lis[b]
    swapper.append([a,b])
    return lis

def right_son(lis,n):
    val = 2*n+2
    if val >= len(lis):
        return False
    else:
        return val

def left_son(lis,n):
    val = 2*n+1
    if val >= len(lis):
        return False
    else:
        return val

def is_leaf(lis,n):
    if (left_son(lis,n) == False) and (left_son(lis,n) == False):
        return True
    else:
        return False


def parent(n):
    if n == 0:
        return 0
    else:
        x = math.floor((n - 1) / 2 )
        return x

# - 1 , -1 - proper order
# return elements to swap
def is_proper(lis,n):

    if is_leaf(lis,n):
        return -1,-1
    else:
        father = n
        l_son = left_son(lis,n)
        r_son = right_son(lis,n)

        if l_son == False:
            if lis[father] <= lis[r_son]:

                return -1,-1
            if lis[father] > lis[r_son]:
                return father, r_son
        elif r_son == False:
            if lis[father] <= lis[l_son]:

                return -1,-1
            if lis[father] > lis[l_son]:
                return father, l_son
        else:

            if min(lis[father],lis[r_son],lis[l_son]) <  lis[father]:
                if lis[r_son] <=lis[l_son]:
                    return father, r_son
                else:
                    return father, l_son

            else:
                return -1,-1

#функция просеиватель листьев
def hipisation(lis,n):
    if is_leaf(lis,n):
        return lis
    else:
        res1 , res2 = is_proper(lis,n)
        if res1 == -1:
            return lis
        else:

            lis = swap(lis,res1,res2)

            lis = hipisation(lis,res2)
        return lis



lis = read_data()
#print(binarytree.build(lis))

r = len(lis)-1

for i in range(r,-1,-1):
    # run operation only for internal nodes (not leafs)
    if is_leaf(lis,i) == False:
        lis = hipisation(lis,i)

#print(swapper)

print(len(swapper))

for sw in swapper:
    print(sw[0],sw[1])





