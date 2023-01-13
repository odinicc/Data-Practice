import math
import string

def isSubsequence(s, t):
    if len(s) > len(t):
        return False
    elif len(s) == 0:
        return True

    else:
        iter = 0
        iter_max = len(s)
        for i in range(len(t)):
            if s[iter] == t[i]:
                if iter == iter_max - 1:
                    return True
                else:
                    iter += 1

    return False

s = "abc"
t = "ababd"
print(isSubsequence(s,t))


