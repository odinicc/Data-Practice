import math
import string

#def isIsomorphic(self, s, t):
def firstUniqChar(s):
    s = list(s)
    md = {}
    m_value = len(s)+1
    alphabet = list(string.ascii_lowercase)
    for a in alphabet:
        md[a] = []
    for r in range(len(s)):
        x = md[s[r]]
        x.append(r)
        md[s[r]] = x
    for letter in md:
        if len(md[letter]) == 1:
            if md[letter][0] < m_value:
                m_value = md[letter][0]

    if m_value > len(s):
        return -1
    else:
        return m_value



s = "loveleetcode"
print(firstUniqChar(s))


#%%
