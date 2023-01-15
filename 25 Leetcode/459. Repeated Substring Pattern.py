import math

#def romanToInt(self, s):
def repeatedSubstringPattern( s):

    n = len(s)
    if n == 1:
        return True
    nod = []
    for i in range(1,n):
        if n%i == 0:
            nod.append(i)
    print(nod)
    for iteration in nod:
        template = s[:iteration]
        for i in range(iteration,n,iteration):
            if template != s[i:i+iteration]:
                break
            if i+iteration == n:
                return True

    return False

s = "a"
print(repeatedSubstringPattern(s))

