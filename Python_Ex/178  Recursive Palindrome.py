x = "ojbbjo"
y = list(x)
print("y = ", y)
l = len(y)
print("l = ", l)

def check_polindrom(y):
    l = len(y)
    if l > 1:
        first = y[0]
        last = y[l-1]
        if first != last:
            print("no polindrom")
        else:
            y.remove(first)
            y.remove(last)
            check_polindrom(y)
    else:
        print("yes polindrom")

check_polindrom(y)

