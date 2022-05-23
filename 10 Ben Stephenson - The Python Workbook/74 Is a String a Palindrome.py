x = input("input string ")
y = list(x)
l = len(x)
for i in range(l):
    if i == l-1:
        print("polindrom")
        break
    elif y[i] != y[l-i-1]:
        print("not polindrom")
        break
