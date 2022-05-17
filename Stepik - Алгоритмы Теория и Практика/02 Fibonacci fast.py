
import sys

def read_data():
    # for local solution
    inf = open('2fib.txt', 'r')

    # for system solution
    # inf = sys.stdin

    Lines = inf.readline().replace('\n', '')
    A = list(Lines.split(" "))
    N = int(A[0])
    return N

def calculate_fib(N):
    Fib_arr = []
    if N > 0:
        Fib_arr.append(1)
    if N > 1:
        Fib_arr.append(1)
    if N > 2:
        for i in range(2, N):
            K = Fib_arr[i - 1] + Fib_arr[i - 2]
            Fib_arr.append(K)
    return Fib_arr[-1]

N = read_data()
Fib = calculate_fib(N)
print(Fib)