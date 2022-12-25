import math


#def plusOne(self, digits):
def plusOne(digits):
    digits = [int(x) for x in digits]
    digits2 = []
    temp = 0
    for i in range(len(digits)-1,-1,-1):

        if digits[i]< 9 and temp == 0:
            if i == len(digits)-1:
                digits2.append(digits[i]+1)
            else:
                digits2.append(digits[i])
            temp = 0
        elif digits[i]< 9 and temp == 1:
            digits2.append(digits[i]+1)
            temp = 0
        elif digits[i] == 9 and temp == 1:
            digits2.append(0)
            temp = 1
        elif digits[i] == 9 and temp == 0:
            if i == len(digits)-1:
                digits2.append(0)
                temp = 1
            else:
                digits2.append(digits[i])

    if temp == 1:
        digits2.append(1)


    return digits2[::-1]



print(plusOne(list('9876543210')))

