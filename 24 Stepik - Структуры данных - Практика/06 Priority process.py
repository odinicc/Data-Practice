

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
proc = []
for i in range(num_proc):
    proc.append(0)

work = []

for i in range(len(lis)):
    #print('proc',proc)
    processor = find_min_proc(proc)
    #print('processor',processor)
    proc_time = proc[processor]
    print(processor, proc_time)
    proc[processor] = proc_time+ lis[i]



    #work.append([processor,])




