
import hashlib
import sys
import math



def read_data():
    #read from file
    inf = open("10 Rabin–Karp algorithm.txt","r")

    #read from system input
    #inf = sys.stdin

    lines = inf.readlines()

    substr = lines[0].rstrip()
    stri =lines[1].rstrip()

    return list(substr) , list(stri)


def hash_f(stri):
    result = hashlib.md5(str(stri).encode())
    return result

# Use Fermat algoithm
def is_prime(num):
    if num == 2:
        return True
    if not num & 1:
        return False
    return pow(2, num-1, num) == 1

def find_max_prime(n):
    if n < 2:
        return 1
    else:
        for i in range(n,0,-1):
            if is_prime(i) == True:
                return i



substr , stri = read_data()

substr_len = len(substr)
target_prime = find_max_prime(substr_len)
hash_substr = hash_f(substr)

print(hash_f(substr).hexdigest())

for i in range(len(stri) -substr_len+1):
    #print(stri[i:i+substr_len])
    hash_cur_string = hash_f(stri[i:i+substr_len])
    if hash_cur_string.hexdigest() == hash_substr.hexdigest():
        if stri[i:i+substr_len] == substr:
            print(i, end =" ")

print('  ')
