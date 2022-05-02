#file_name = input('give me file name ')
inf = open('hamlet2.txt', 'r')

outf = open('result.txt', "w")

Lines = inf.readlines()
k = len(Lines)
for i in range(k):
    L = " - " + str(Lines[i])
    outf.write(L)