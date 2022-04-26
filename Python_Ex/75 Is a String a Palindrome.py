x = input("input string ")
y = list(x)
y = list(filter(None, y))
l = len(x)
for i in range(l):
    if i == l-1:
        print("polindrom")
        break
    elif y[i] != y[l-i-1]:
        print("not polindrom")
        break
