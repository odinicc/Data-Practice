
import sys
import pprint

def read_data():
    # for local solution
    inf = open('2fib_mod.txt', 'r')

    # for system solution
    # inf = sys.stdin

    Lines = inf.readline().replace('\n', '')
    A = list(Lines.split(" "))
    N = int(A[0])
    mod = int(A[1])
    return N , mod

def calculate_fib(N,mod):
    Fib_arr = []
    Mod_arr = []
    Mod_arr2 = []
    if N > 0:
        Fib_arr.append(1)
        Mod_arr2.append(1)
    if N > 1:
        Fib_arr.append(1)
        Mod_arr2.append(1)
        prev = 1
    if N > 2:
        for i in range(2, N):
            K = Fib_arr[i - 1] + Fib_arr[i - 2]
            Fib_arr.append(K)
            M = (Fib_arr[i - 1] + Fib_arr[i - 2])%mod
            Mod_arr2.append(M)
            Mod_arr.append([i,K,M])
             

    pprint.pprint(Mod_arr)
    return Fib_arr[-1]

N ,mod = read_data()
print(mod)
Fib = calculate_fib(N,mod)
