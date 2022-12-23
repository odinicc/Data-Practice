
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




substr , stri = read_data()

substr_len = len(substr)
hash_substr = hash_f(substr)


for i in range(len(stri) -substr_len+1):
    hash_cur_string = hash_f(stri[i:i+substr_len])
    if hash_cur_string.hexdigest() == hash_substr.hexdigest():
        if stri[i:i+substr_len] == substr:
            print(i, end =" ")

print('  ')
