import re
import pprint
file_name = "hamlet.txt"
inf = open(file_name, 'r')

Lines = inf.readlines()
k = len(Lines)
print('Lines',Lines)
Words_by_letter = {}
for row in range(k):
    words = Lines[row].split(" ")
    for word in words:
        word = word.replace('\n', '').replace('\t', '').replace('-', '').replace('[', '')
        word = re.sub("[!,*)@#%(&$_?.^]", '', word)
        try:
            First_letter = word[0]
            Code_First_letter = ord(First_letter)
            if 123 > Code_First_letter > 96:
                Code_First_letter = Code_First_letter - 32
                First_letter = chr(Code_First_letter)

            if First_letter in Words_by_letter:
                Words_by_letter[First_letter] += 1
            else:
                Words_by_letter[First_letter] = 1
        except:
            print("Error word ",word)


pprint.pprint(Words_by_letter)
