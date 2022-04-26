a = input("enter the word ")

ch = list(a)
#convert string to list 
for i in range(len(ch)):
    o  = ord(ch[i])
    if 96 < o <= 119:
        o = o + 3
        ch[i] = chr(o)
    elif 119 < o < 123:
        o = o - 23
        ch[i] = chr(o)
#convert list to string
str1 = ''.join(ch)
print(str1)
#abcdefghijklmnopqrstuvwxyz
