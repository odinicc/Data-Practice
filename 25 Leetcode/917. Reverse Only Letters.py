import math
import re

#def romanToInt(self, s):

def reverseOnlyLetters(self, s):
    s = list(s)
    first_iter = 0
    first_letter = 0
    last_iter = len(s)-1
    last_letter = len(s)
    while first_iter<last_iter:
        if s[first_iter].isalpha() and s[last_iter].isalpha():
            s[first_iter] , s[last_iter] = s[last_iter] , s[first_iter]
        if s[first_iter].isalpha() == False:
            first_iter += 1
        if s[last_iter].isalpha() == False:
            last_iter -= 1
    return s


s = "ab-cd"
print(reverseOnlyLetters(s))
