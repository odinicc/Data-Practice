import string

def numberOfLines(widths, s):
    alphabet = list(string.ascii_lowercase)
    al_d = {}
    for i in range(len(alphabet)):
        al_d[alphabet[i]] = widths[i]
    print(al_d)

    line_iter = 0
    row_iter = 1
    for symb in s:
        if line_iter + al_d[symb] > 100:
            line_iter = 0
            row_iter += 1

        line_iter += al_d[symb]
    print(row_iter,line_iter)







widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s = "abcdefghijklmnopqrstuvwxyz"
print(numberOfLines(widths, s))
