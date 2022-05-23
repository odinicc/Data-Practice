list1 = ['1','3','4','5','6','7']
list2 = ['5','6','7']
st = '21324'

x = all(i in list1 for i in list2)

print("x = ",x)

y = [i+i for i in range(len(list2))]
z = [ i in list1 for i in list2 ]

print("y = ",y)
print("z = ",z)


def isSublist(list1 , list2):
    l1 = ''.join(list1)
    l2 = ''.join(list2)
    print("l1 = ",l1)
    print("type(l1) = ",type(l1))
    print("l2 = ",l2)
    #m =  st.find('2')
    m =  l1.find(l2)
    print("m = ",m)
    



isSublist(list1 , list2)
