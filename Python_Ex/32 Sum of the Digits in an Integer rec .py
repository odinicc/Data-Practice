a = input("Enter the int value")

def leng(y):
    fl = list(y)
    x=0
    for i in range (0, len(fl)):
        x = x + int( fl[i] )
    return x

def convert(a):
    if len(a) == 1:
        return a
    else:
        return convert( str(leng(a)) )

z = convert(str(a))

print("z =", z)
    
