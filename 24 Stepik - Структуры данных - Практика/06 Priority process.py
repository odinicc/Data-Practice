

import sys
import math



def read_data():
    #read from file
    inf = open("06 Priority process.txt","r")

    #read from system input
    #inf = sys.stdin

    lines = inf.readlines()

    lis = lines[1].rstrip('\n')

    inf.close()
    lis = lis.split()
    lis = list(map(int, lis))

    return lis










