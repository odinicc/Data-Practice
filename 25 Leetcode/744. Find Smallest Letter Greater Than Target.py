import math

#def longestCommonPrefix(self, strs):
def nextGreatestLetter(letters, target):
    alph = "abcdefghijklmnopqrstuvwxyz"
    letters_index = [alph.index(x) for x in letters]
    target_index = alph.index(target)
    smalest = 30
    for x in letters_index:
        if x > target_index and x < smalest:
            smalest = x


    return alph[smalest]



letters = ["c","f","j"]
target = "a"
print(nextGreatestLetter(letters, target))


