file_name = 'hamlet.txt'

fl = open(file_name, 'r')
print('fl', fl)
Lines = fl.readlines()
print('Lines', Lines)
wword_ie_true = []
wword_ie_wrong = []
wword_ei_true = []
wword_ei_wrong = []
for row in range(len(Lines)):
    words = Lines[row].split(" ")
    for word in words:
        word = word.replace('\n', '').replace('.', '').replace(',', '').replace('"', '').replace('  ', '')
        if 'ie' in word:
            ie = word.find('ie')
            before_ie = word[ie-1]
            if before_ie == "c" or before_ie == "C":
                wword_ie_wrong.append(word)
            else:
                wword_ie_true.append(word)
        if 'ei' in word:
            ei = word.find('ei')
            before_ei = word[ei-1]
            if before_ei != "c" and before_ei != "C":
                wword_ei_wrong.append(word)
            else:
                wword_ei_true.append(word)




#def symbol_before_ei(word):


print('wword_ie_true',wword_ie_true)
print('wword_ei_true',wword_ei_true)
print('wword_ie_wrong',wword_ie_wrong)
print('wword_ei_wrong',wword_ei_wrong)