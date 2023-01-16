import math

def findContentChildren(g, s):
    g.sort()
    s.sort()
    count = 0
    ck = len(s)-1
    for i in range(len(g)-1,-1,-1):
        if ck < 0:
            break
        if g[i] <= s[ck]:
            count += 1
            ck -= 1

    return count



g = [2,2,3]
s = [1]
print(findContentChildren(g,s))



#%%
