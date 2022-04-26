
a = " enter the i yes? word "

def capitalize(a):

    ch = list(a)

    # Capitalize the first non-space character
    for i in range(len(ch)-1):
        if ch[i] != " ":
            ch[i] = ch[i].upper()
            break

    # Capitalize the first non-space character after a period  exclamation mark or question mark
    for i in range(len(ch)-1):
        if ch[i] == "?" or ch[i] == "!":
            for k in range(i+1 , len(ch)-1):
                if ch[k] != " ":
                    ch[k] = ch[k].upper()
                    break

    #Upper case i
    for i in range(len(ch)-3):
        if ch[i] == " " and ch[i+1] == "i" and ch[i+2] == " ":
            ch[i+1] = ch[i+1].upper()
    str1 = ''.join(ch)
    return str1 

print(a)
print(capitalize(a))



