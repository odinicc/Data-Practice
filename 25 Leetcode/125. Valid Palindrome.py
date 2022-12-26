import math

#def isPalindrome(self, s):
def isPalindrome(s):
    lis = list(s)
    filtered = []
    for i in lis:
        if  64 < ord(i) and ord(i) < 91:
            filtered.append(i.lower())
        elif 96 < ord(i) and ord(i) < 123:
            filtered.append(i)
        elif 47 < ord(i) and ord(i) < 58:
            filtered.append(i)
    l = len(filtered)
    for i in range(l//2):
        if filtered[i] != filtered[l-i-1]:
            return False

    return True



print(isPalindrome(''))

