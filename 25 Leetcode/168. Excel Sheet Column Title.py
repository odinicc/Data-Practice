import math

#def convertToTitle(self, columnNumber):
def convertToTitle(columnNumber):
    linked = []
    ost = columnNumber
    while  ost > 26:
        new_ost = ost % 26
        if new_ost == 0:
            new_ost = 26
        linked.append(new_ost)
        ost = (ost - new_ost)/26

    linked.append(ost)

    result = []
    for i in range(len(linked)):
        m = linked[i]
        result.append(chr(64+int(m)))
    result.reverse()
    s = ''.join(result)
    return s

print(convertToTitle(28))


