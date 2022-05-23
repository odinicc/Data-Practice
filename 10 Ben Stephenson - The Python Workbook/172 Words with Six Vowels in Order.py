import re
from tqdm import tqdm
import pprint

vovels = ['a','e','i','o','u']

file_name = "unigram_freq.csv"
inf = open(file_name, 'r')
Lines = inf.readlines()

lis = []
vov_words = []
for word in tqdm(Lines):
    words = word.split(",")
    lis.append(words[0])

for i in range(len(lis)):
    word = lis[i]
    for k in range(len(word)):
        #print(word[k])
        if word[k] not in vovels:
            break
        if k == len(word) - 1:
            vov_words.append(word)


pprint.pprint(vov_words)