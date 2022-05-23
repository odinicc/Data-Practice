
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


def calculate_pisano_period3(mod,N):
    N = max(N,mod*6)
    if mod == 1:
        return 1, [0]
    else:
        M_prev = 1
        M_curr = 1
        Mod_arr = [0, 1, 1]
        for i in range(2,N):
            M_curr , M_prev = (M_curr + M_prev)%mod , M_curr
            Mod_arr.append(M_curr)
            if M_curr == 1 and M_prev == 0:
                break

    Mod_arr.pop()
    Mod_arr.pop()
    return i ,Mod_arr



def calculate_feb(N):
    prev = 1
    curr = 1
    if N<3:
        return 1
    else:
        for i in range(2,N):
            prev ,curr = curr, prev + curr

    return curr



N ,mod = read_data()
N = 60282445765134413
mod = 2263
#print(N,mod)
period , Mod_arr = calculate_pisano_period3(mod,N)
#print("period ",period)
#print("Mod_arr ",*Mod_arr)
N_min = N%period
X = Mod_arr[N_min]
print(X)