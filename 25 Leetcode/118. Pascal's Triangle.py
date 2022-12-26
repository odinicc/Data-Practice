import math

#def generate(self, numRows):
def generate(numRows):
    if numRows == 0:
        return ""
    if numRows == 1:
        return [[1]]
    overal = [[1]]
    temp = [1]
    for i in range(1,numRows):
        temp_next = []
        for j in range(len(temp)+1):

            if j == 0 or j == len(temp):
                temp_next.append(1)
            else:
                temp_next.append(temp[j]+temp[j-1])
        overal.append(temp_next)
        temp = temp_next

    return overal


print(generate(5))


