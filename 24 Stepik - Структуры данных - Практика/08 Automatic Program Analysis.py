

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

    equal = []
    for line in lines[1:equal_num+1]:
        el = line.rstrip('\n')
        equal.append([el[0],el[2]])

    non_equal = []
    print('--------------------------')
    for line in lines[equal_num+1:]:
        el = line.rstrip('\n')
        non_equal.append([el[0],el[2]])

    inf.close()
    return equal , non_equal


equal , non_equal  = read_data()
print(equal)
print(non_equal)

main_set = set()

for eq in equal:
    main_set.add(eq[0])
    main_set.add(eq[1])

print(main_set)

for neq in non_equal:
    if (neq[0] in main_set) and (neq[1] in main_set):
        return



