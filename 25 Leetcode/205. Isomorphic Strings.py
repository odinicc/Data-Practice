import math

#def isIsomorphic(self, s, t):
def isIsomorphic(s, t):
    dic = {}
    for i in range(len(s)):)
        if s[i] in dic.keys():
            key = s[i]
            new_val = t[i]
            old_val = dic[key]
            if new_val != old_val:
                return False
        elif s[i] not in dic.keys():
            if t[i] not in dic.values():
                dic[s[i]] = t[i]
            elif t[i] in dic.values():
                    return False
    return True

s = "edd"
t = "afd"
print(isIsomorphic(s, t))


#%%
