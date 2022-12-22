
import queue

import sys
import math



def read_data():
    #read from file
    inf = open("06 Priority process.txt","r")

    #read from system input
    #inf = sys.stdin

    lines = inf.readlines()

    f = lines[0].rstrip('\n')
    fir =f.split(' ')
    num_proc = int(fir[0])
    s = lines[1].rstrip('\n')

    lis = s.split(' ')
    lis = [int(x) for x in lis]

    inf.close()
    return num_proc , lis


def find_min_proc(proc):
    min_proc = 0
    for i in range(len(proc)):
        if proc[i] < proc[min_proc]:
            min_proc = i

    return min_proc



num_proc, lis = read_data()

#print('num_proc',num_proc)
proc = queue.PriorityQueue()
for i in range(num_proc):
    proc.put((0,i))

work = []


for i in range(len(lis)):
    #print(proc.queue)
    #find element(time,processor) with min minimum time
    elem = proc.get()
    print(elem[1],elem[0])
    new_time = elem[0] + lis[i]

    new_proc = elem[1]
    proc.put((new_time,new_proc))





