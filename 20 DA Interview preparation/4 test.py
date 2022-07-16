from re import L
from tenacity import retry


m = 66
def compresss(m):
    n = m
    for i in range(m):
        l = list(str(n))
        if len(l) == 1:
            return l 
        else:
            l = [int(i) for i in l]
            n = sum(l)

print(compresss(m))
