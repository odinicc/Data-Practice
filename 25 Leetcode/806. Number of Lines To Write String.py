import math
import re

#def romanToInt(self, s):

def mostCommonWord( paragraph, banned):
    #paragraph = paragraph.replace('!','').replace('?','').replace("'",'').replace(',','').replace(';','').replace('.','')
    paragraph = re.split("[!?',;. ]",paragraph)
    paragraph = list(filter(lambda x: (len(x) > 0), paragraph))
    paragraph = [w.lower() for w in paragraph]
    print(paragraph)
    word_dic = {}
    for word in paragraph:
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1
    for ban in banned:
        if ban in word_dic:
            word_dic[ban] = 0


    max_count = 0
    for word in word_dic:
        if word_dic[word] > max_count:
            max_count = word_dic[word]
            max_word = word
    return max_word





paragraph = 'a, a, a, a, b,b,b,c, c'
banned = ["a"]
print(mostCommonWord( paragraph, banned))
