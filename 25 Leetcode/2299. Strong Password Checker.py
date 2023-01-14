import math
import re

#def romanToInt(self, s):

def strongPasswordCheckerII(password):
    if len(password) <8:
        print(1)
        return False
    if bool(re.search(r"[0-9]", password)) == False:
        print(2)
        return False
    if bool(re.search(r"[A-Z]", password)) == False:
        print(3)
        return False
    if bool(re.search(r"[a-z]", password)) == False:
        print(4)
        return False
    if bool(re.search(r"[!@#$%^&*()-+]", password)) == False:
        print(5)
        return False
    for i in range(len(password)-1):
        if password[i] == password[i+1]:
            print(6)
            return False


    return True
print(1)
password = "-Aa1a1a1"
print(strongPasswordCheckerII(password))

