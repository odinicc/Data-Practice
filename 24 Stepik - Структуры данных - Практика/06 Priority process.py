

import sys
import math



def read_data():
    #read from file
    inf = open("06 Priority process.txt","r")

    #read from system input
    #inf = sys.stdin

    lines = inf.readlines()

    f = lines[0].rstrip('\n')
    num_proc = int(f[0])
    s = lines[1].rstrip('\n')

    lis = s.split(' ')

    inf.close()
    return num_proc , lis


def find_min_proc(proc):
    min_proc = 0
    for i in range(len(proc)-1):
        if proc[i] < proc[min_proc]:
            min_proc = i

    return min_proc


print(find_min_proc([3,3,4]))

num_proc, lis = read_data()


proc = []
for i in range(num_proc):
    proc.append(0)

work = []

#for i in range(len(lis)):
#    for pr in proc:


#print(num_proc)
#print(lis)

