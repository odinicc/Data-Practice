

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
    first_row = lis.split(' ')
    equal_num = int(first_row[1])
    #print(equal_num,' - equal_num')
    #print('first_row',first_row)

    equal = []
    for line in lines[1:equal_num+1]:
        el = line.rstrip('\n')
        equal.append([el[0],el[2]])

    non_equal = []
    for line in lines[equal_num+1:]:
        el = line.rstrip('\n')
        non_equal.append([el[0],el[2]])

    inf.close()
    return equal , non_equal

def algo_checker(equal,non_equal):
    main_set = set()

    for eq in equal:
        main_set.add(eq[0])
        main_set.add(eq[1])

    for neq in non_equal:
        if (neq[0] in main_set) and (neq[1] in main_set):
            return 0
        #this will check situations when variable compared with itself
        #for example 5 != 5
        if (neq[0] == neq[1]):
            return 0

    return 1




equal , non_equal  = read_data()
#print(equal)
#print(non_equal)

print(algo_checker(equal,non_equal))



