import math

#def romanToInt(self, s):
def findTheDifference(s, t):

    if len(s) == 0:
        return t[0]

    s = list(s)
    t = list(t)
    s_i = 0
    t_i = 0
    diff = []
    while s_i <  len(s):
        if s[s_i] == t[t_i]:
            s_i += 1
            t_i += 1
        else:
            diff.append(t[t_i])
            t_i += 1
        if s_i == len(s) and t_i != len(t):
            diff = diff+t[t_i:]
    return diff[0]

s = ""
t = "ax"
print(findTheDifference(s, t))
