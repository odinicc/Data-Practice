import math

#def isPalindrome(self, x)
def isPalindrome(x):
    str_x = list(str(x))

    l = len(str_x)
    if l == 0:
        return False
    for i in range(l//2):
        if str_x[i] != str_x[l-i-1]:
            return False
    return True


print(isPalindrome(''))

