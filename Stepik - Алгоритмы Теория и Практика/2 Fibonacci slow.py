from recviz import recviz
from functools import lru_cache
import time




def fib(n):
    if n<2:
        return n
    else:
        return fib(n-1) + fib(n-2)

n = 20
#print("fib(n) = ", fib(n),"n = ",n)

fib3 = lru_cache(maxsize=None)(fib)


cache = {}
#@recviz
def fib2(n):
    if n not in cache:
        if n < 2:
            return n
        else:
            return fib2(n-1) + fib2(n-2)
    else:
        return cache[n]

print("fib2(n) = ", fib2(n),"n = ",n)
print("fib3(n) = ", fib3(n),"n = ",n)


def fib4(n):
    f0 = 0
    f1 = 1
    for i in range (n-1):
        f0,f1 = f1,f0+f1
    return f1

print("fib4(100)", fib4(100))

def timed(f, *args, n_iter=100):
    acc = float("inf")
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1 - t0)
    return acc

print(timed(fib4,900))