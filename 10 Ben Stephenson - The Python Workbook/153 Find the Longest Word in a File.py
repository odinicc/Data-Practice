file_name = "hamlet2.txt"
inf = open(file_name, 'r')

Lines = inf.readlines()
k = len(Lines)
print('Lines',Lines)
maxword_len = 0
for row in range(k):
    words = Lines[row].split(" ")
    for word in words:
        word = word.replace('\n', '').replace('.', '').replace(',', '').replace('"', '')
        #print(word)
        if len(word)>maxword_len:
            maxword_len = len(word)
            maxword = word

print(' Maxword ',maxword,'with max len',maxword_len)