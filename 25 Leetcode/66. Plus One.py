import math


#def plusOne(self, digits):
def plusOne(digits):
    digits = [int(x) for x in digits]
    digits2 = []
    temp = 1
    for i in range(len(digits)-1,-1,-1):
        print('i = ',i)
        if digits[i]+ temp < 9:
            digits2.append(digits[i]+temp)
            temp = 0
        else:
            digits2.append(0)
            temp = 1

    if temp == 1:
        digits2.append(1)

    return digits2[::-1]



print(plusOne(list('9')))

