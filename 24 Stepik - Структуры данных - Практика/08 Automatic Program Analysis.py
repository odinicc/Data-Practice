

import sys
import math

swapper = []

def read_data():
    #read from file
    inf = open("08 Automatic Program Analysis.txt","r")

    #read from system input
    #inf = sys.stdin

    lines = inf.readlines()

    lis = lines[0].rstrip('\n')
    first_row = lis.split()
    equal_num = int(first_row[1])
    print(first_row[1])
    print(type(lines))

    equal = []
    for line in lines[1:equal_num+1]:
        print(line)

    non_equal = []
    print('--------------------------')
    for line in lines[equal_num+1:]:
        print(line)


    inf.close()


    return lis




lis = read_data()
#print(binarytree.build(lis))






