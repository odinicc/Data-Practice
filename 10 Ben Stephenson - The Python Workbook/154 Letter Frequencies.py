import pprint

file_name = "hamlet2.txt"
inf = open(file_name, 'r')

Lines = inf.readlines()
k = len(Lines)
print('Lines',Lines)
letter_freq = {}
for row in range(k):
    words = list(Lines[row])
    for symbol in words:
        symbol_code = ord(symbol)
        if 64 < symbol_code < 90 :
            if symbol in letter_freq:
                letter_freq[symbol] +=1
            else:
                letter_freq[symbol] = 1

        elif 96 < symbol_code < 123:
            Large_sumbol = chr(symbol_code-32)
            if Large_sumbol in letter_freq:
                letter_freq[Large_sumbol] +=1
            else:
                letter_freq[Large_sumbol] = 1



pprint.pprint(letter_freq)