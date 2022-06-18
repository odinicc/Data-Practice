from re import L
import sys

def recur(n):
    for i in range(n):
        ar = list(str(n))
        if len(ar) == 1:
            return ar[0]
            break
        n = 0
        for i in ar:
            n = n + int(i)


m = recur(651)
print("m = ", m)