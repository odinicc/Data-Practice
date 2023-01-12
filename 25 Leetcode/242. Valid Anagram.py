import math
import string

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    else:
        alphabet = list(string.ascii_lowercase)
        s_dic = {}
        t_dic = {}
        for m in alphabet:
            s_dic[m] = 0
            t_dic[m] = 0
        for i in range(len(t)):
            s_dic[s[i]] += 1
            t_dic[t[i]] += 1
        for m in alphabet:
            if s_dic[m] != t_dic[m]:
                return False
        return True


s = "anagram"
t = "nagaram"
print(isAnagram(s,t))


