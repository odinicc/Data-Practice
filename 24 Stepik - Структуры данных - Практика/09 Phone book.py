

import sys
import math

swapper = []

def read_data():
    #read from file
    inf = open("09 Phone book.txt","r")

    #read from system input
    #inf = sys.stdin

    lines = inf.readlines()

    lis = []
    for line in lines[1:]:
        el = line.rstrip('\n')
        el2 = el.split(' ')
        lis.append(el2)

    return lis



lis  = read_data()
phone_book = {}
for lis_item in lis:
    if lis_item[0] == 'add':
        phone_book[lis_item[1]] = lis_item[2]
    elif lis_item[0] == 'find':
        if lis_item[1] in phone_book:
            print(phone_book[lis_item[1]])
        else:
            print('not found')

    elif lis_item[0] == 'del':
        if lis_item[1] in phone_book:
            del phone_book[lis_item[1]]



