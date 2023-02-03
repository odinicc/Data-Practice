import math


#def plusOne(self, digits):

def vp(s):
    l = len(s)
    for i in range(l//2):
        if s[i] != s[l-1-i]:
            return False
    return True


def validPalindrome(s):
    l = len(s)
    for i in range(l//2):
        if s[i] != s[l-1-i]:
            #print(s[:i]+s[i+1:],'--- ',s[:l-1-i]+s[l-i:])
            if vp(s[:i]+s[i+1:]) == True:
                return True
            if vp(s[:l-1-i]+s[l-i:]) == True:
                return True
            return False

    return False


s = "abbbcba"
print(vp(s))

print(validPalindrome(s))


