
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





substr , stri = read_data()

substr_len = len(substr)


