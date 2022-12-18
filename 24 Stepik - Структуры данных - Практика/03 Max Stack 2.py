

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

def cust_append(stack,track_stack,element):
    stack.append(int(element))
    if len(track_stack) == 0:
        track_stack.append(int(element))
    else:
        if int(element) > track_stack[-1]:
            track_stack.append(int(element))
        else:
            track_stack.append(track_stack[-1])
    return stack, track_stack

def cust_pop(stack,track_stack):
    stack.pop()
    track_stack.pop()
    return stack, track_stack

def cust_max(stack,track_stack):
    if len(stack)>0:
        return(track_stack[-1])
    else:
        return 0

def max_result(s):
    stack = []
    track_stack = []
    max_stack = []
    for i in range(len(s)):
        if s[i][0] == 'push':
            stack, track_stack  = cust_append(stack,track_stack,s[i][1])
        elif s[i][0] == 'pop':
            if len(stack)>0:
                stack, track_stack = cust_pop(stack,track_stack)
        elif s[i][0] == 'max':
            max_stack.append(cust_max(stack,track_stack))
    print(track_stack)
    return  max_stack


s = read_data()

print(*max_result(s), sep="\n")





