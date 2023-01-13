import math

#def romanToInt(self, s):
def licenseKeyFormatting(s, k):
    if len(s)<k:
        return s

    s = s.replace('-','')
    s = s.upper()
    res = ''
    n = len(s)
    print(s)
    for i in range(n,k-1,-k):
        res = s[i-k:i] + '-' + res
    res = res[:-1]
    if n%k != 0:
        print('--',s[0:n%k])
        res = s[0:n%k] + '-' + res
    return res

s = "2-5g-3-J"
k = 2
print(licenseKeyFormatting(s, k))
