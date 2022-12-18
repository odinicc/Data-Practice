

import math
import sys

def read_data():
    #read from file
    inf = open("03 Max Stack.txt","r")

    #read from system input
    #inf = sys.stdin

    l = []
    Lines  = inf.readlines()[1:]
    for line in Lines:
        l.append(list(line.rstrip('\n').split(" ")))

    return l

def cust_append(stack,element):
    x = stack.append(int(element))
    return x


def max_result(s):
    stack = []
    max_stack = []
    max_value = 0
    for i in range(len(s)):
        if s[i][0] == 'push':
            stack = cust_append(stack,s[i][1])

        elif s[i][0] == 'pop':
            if len(stack)>0:
                stack.pop()
        elif s[i][0] == 'max':
            if len(stack)>0:
                max_stack.append(max(stack))
            else:
                max_stack.append(0)
    return  max_stack


s = read_data()

print(*max_result(s), sep="\n")





