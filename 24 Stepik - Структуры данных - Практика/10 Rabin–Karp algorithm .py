

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
        hash = hash*256 + ord(stri[i])
    return hash%n

# Use Fermat algoithm
def is_prime(num):
    if num == 2:
        return True
    if not num & 1:
        return False
    return pow(2, num-1, num) == 1

def find_max_prime(n):
    for i in range(n,0,-1):
        if is_prime(i) == True:
            return i



substr , stri = read_data()

target_prime = find_max_prime(len(substr))
print(target_prime)

print( hash_f(substr,15) )


print(is_prime(10))
