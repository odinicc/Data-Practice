import math
import string
import sys


def readfile():
    inf = open("file.txt","r")
    l = []
    Lines  = inf.readlines()
    for line in Lines:
        l.append(line.rstrip('\n'))
    return l

def filter(s):
    if s[0].isdigit():
        if s[1].isdigit() and s[2].isdigit()\
                and s[3] == '-' and\
                s[4].isdigit() and s[5].isdigit() and s[6].isdigit() \
                and s[7] == '-' \
                and s[8].isdigit()  and s[9].isdigit() and s[10].isdigit()  and s[11].isdigit() \
                and len(s) == 12:
            return True
        else:
            return False
    elif s[0] == '(':
        if s[1].isdigit() and s[2].isdigit() and s[3].isdigit() \
            and s[4] == ')'\
            and s[5] == ' '\
            and s[6].isdigit() and s[7].isdigit() and s[8].isdigit() \
            and s[9] == '-' \
            and s[10].isdigit() and s[11].isdigit() and s[12].isdigit():
            return True
        else:
            return False

    else:
        return False

f = readfile()
for num in f:
    if filter(num) == True:
        #print(num)
        sys.stdout.write(num)
        sys.stdout.write('\n')


