
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

def z_function(stri):
    l = len(stri)
    z = [0] * l
    n = len(stri)

    # [L,R] make a window which matches
    # with prefix of s
    l, r, k = 0, 0, 0
    for i in range(1, n):

        # if i>R nothing matches so we will calculate.
        # Z[i] using naive way.
        if i > r:
            l, r = i, i

            # R-L = 0 in starting, so it will start
            # checking from 0'th index. For example,
            # for "ababab" and i = 1, the value of R
            # remains 0 and Z[i] becomes 0. For string
            # "aaaaaa" and i = 1, Z[i] and R become 5
            while r < n and stri[r - l] == stri[r]:
                r += 1
            z[i] = r - l
            r -= 1
        else:

            # k = i-L so k corresponds to number which
            # matches in [L,R] interval.
            k = i - l

            # if Z[k] is less than remaining interval
            # then Z[i] will be equal to Z[k].
            # For example, str = "ababab", i = 3, R = 5
            # and L = 2
            if z[k] < r - i + 1:
                z[i] = z[k]

            # For example str = "aaaaaa" and i = 2,
            # R is 5, L is 0
            else:

                # else start from R and check manually
                l = i
                while r < n and stri[r - l] == stri[r]:
                    r += 1
                z[i] = r - l
                r -= 1

    return z

def z_search(pattern,text):
    concat = pattern + ["$"] + text
    l = len(concat)
    z = z_function(concat)
    for i in range(l):
        if z[i] == len(pattern):
            print(i - len(pattern) -1,end = ' ')


substr , stri = read_data()


z_search(substr, stri)
print(' ',end = '')
