import re
from tqdm import tqdm

x = "Contractions gooooof include: don’t, isn’t, and wouldn’t."
print(" x = ", x)

file_name = "unigram_freq.csv"
inf = open(file_name, 'r')
Lines = inf.readlines()
k = len(Lines)

lis = []
error = []
for word in tqdm(Lines):
    words = word.split(",")
    lis.append(words[0])

#print(lis)
def only_words(x):
    res = x.split()
    for i in range(len(res)):
        res[i] = re.sub('[,:;.]', '', res[i])
        #print(res[i])
        if res[i] not in lis:
            print("Error, word", res[i],"may be wrong")


only_words(x)