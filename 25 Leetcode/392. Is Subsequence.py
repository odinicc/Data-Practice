import math
import string

def isSubsequence(pattern, s):
    s = s.split(' ')
    if len(s) != len(pattern):
        return False
    else:
        print(map(pattern.find, s))



pattern = "abba"
s = "dog cat cat fish"
print(wordPattern(pattern ,s))


