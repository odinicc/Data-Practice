

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


def hash_f(stri,n):
    hash = 0
    for i in range(len(stri)):
        hash = hash*126 + ord(stri[i])
    return hash%n

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
hash_substr = hash_f(substr,target_prime)


for i in range(len(stri) -substr_len+1):
    #print(stri[i:i+substr_len])
    hash_cur_string = hash_f(stri[i:i+substr_len],target_prime)
    if hash_cur_string == hash_substr:
        if stri[i:i+substr_len] == substr:
            print(i, end =" ")

print('  ')
