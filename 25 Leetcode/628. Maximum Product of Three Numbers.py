import math


#def lengthOfLastWord(self, s):
def lengthOfLastWord(s):
    arrr = s.split(' ')
    for i in range(len(arrr)-1,-1,-1):
        if arrr[i] != '':
            return len(str(arrr[i]))
    return 0

print(lengthOfLastWord("d"))


