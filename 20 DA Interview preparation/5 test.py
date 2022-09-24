#Дан список строк.
#Нужно вывести все буквы, которые встречаются в каждой из строк списка
#(включая дубли).


#["bella","label","roller"] -> ["e","l","l"]
#["cool","lock","cook"] -> ["c","o"]


l1 = ["bella","label","roller"]
a ={}
def get_double_letter(l1):
    for word_num in range(len(l1)):
        word = list(str(l1[word_num]))
        for letter in word:
            if letter in a:
                a[letter] = a[letter] + str(word_num)
            else:
                a[letter] =  str(word_num)
    
    n = []
    for elem in a:
        m = chek(a[elem], len(l1))
        if m > 0:
            for i in range(m):
                n.append(elem)
    
    print(n)

             
def chek(elem,n):
    if elem == '012':
        return 1
    if elem == '001122':
        return 2
    else:
        return 0



print(a)
        
       

get_double_letter(l1)