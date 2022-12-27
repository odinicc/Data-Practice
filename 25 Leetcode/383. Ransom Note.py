import math


def canConstruct(ransomNote, magazine):
    note = list(ransomNote)
    mag = list(magazine)
    mac
    for i in range(len(note)):
        if not note[i] in mag:
            return False
        else:
            mag.remove(note[i])

    return True



ransomNote = "dfd"
magazine = ""
print(canConstruct(ransomNote, magazine))


