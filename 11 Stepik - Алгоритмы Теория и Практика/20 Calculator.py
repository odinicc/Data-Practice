import pprint
import sys

def read_data():
    # for local solution
    inf = open('20.txt', 'r')

    # for system solution
    # inf = sys.stdin

    Lines = inf.readline().replace('\n', '')
    A = list(Lines.split(" "))
    N = int(A[0])
    return N

def create_code(N):
    A_code = []
    for i in range(N+1):
        A_code.append(None)

    A_code[1] = 0
    val = 0
    while A_code[N] == None:
        val += 1
        for j in range(1,N+1):
            if A_code[j] == val-1:
                if j * 3 <= N:
                    if A_code[j * 3] == None:
                        A_code[j * 3] = val
                if j * 2 <= N:
                    if A_code[j * 2] == None:
                        A_code[j * 2] = val
                if j+1 <= N:
                    if A_code[j + 1] == None:
                        A_code[j + 1] = val

    return A_code , A_code[N]

def find_seq(A_code):
    Seq = [None] * (M + 1)
    Seq[M] = N
    Seq[0] = 1
    curr = N
    for k in range(M - 1, 0, -1):
        # print("curr = ", curr)
        prev_arr = []
        for i in range(curr):
            if A_code[i] == k:
                prev_arr.append(i)

        for m in prev_arr:
            if m == curr - 1 or m * 2 == curr or m * 3 == curr:
                Seq[k] = m
                break
        # print("prev_arr", prev_arr , "m = ",m , "curr = ",curr)
        curr = m
    return Seq

N = read_data()
A_code,M = create_code(N)
Seq = find_seq(A_code)

print(A_code[N])
print(*Seq)