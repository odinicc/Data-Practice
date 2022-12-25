import math


#def mergeTwoLists(self, list1, list2):
def mergeTwoLists(list1, list2):
    stack = []
    l1 = len(list1)
    l2 = len(list2)

    if l1 == 0:
        return list2
    elif l2 == 0:
        return list1
    else:
        l1_l = list1[-1]
        l2_l = list2[-1]
        for i in range(l1+l2):
            #print('stack= ',stack,' list1 = ',list1,' list2 =  ',list2 ,' l1_l = ' ,l1_l,' l2_l = ' ,l2_l)
            if l1_l > l2_l:
                stack.append(list1.pop())
                if len(list1) > 0:
                    l1_l = list1[-1]
                else:
                    stack = stack + list2[::-1]
                    return stack[::-1]
            else:
                stack.append(list2.pop())
                if len(list2) > 0:
                    l2_l = list2[-1]
                else:
                    stack = stack + list1[::-1]
                    return stack[::-1]
        return stack[::-1]



list1 = [3]
list2 = [1,2]
print(mergeTwoLists(list1,list2))
