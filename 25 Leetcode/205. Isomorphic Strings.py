import math

#def isIsomorphic(self, s, t):
def isIsomorphic(s, t):
    dic = {}
    for i in range(len(s)):
        print(dic , s[i],t[i])
        if s[i] in dic.keys():
            val = dic[s[i]]
            print('val',val ,'t[i]',t[i] )
            if t[i] != val:
                return False
        elif t[i] in dic.values():
            print('t[i] ' ,t[i])
            key = None
            for j in dic.keys():
                if dic[j] == t[i]:
                    key = t[i]
            if key != s[i]:
                return False


        else:
            dic[s[i]] = t[i]
    return True

s = "egd"
t = "add"
print(isIsomorphic(s, t))


#%%
