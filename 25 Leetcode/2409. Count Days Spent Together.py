import math
from datetime import datetime



#def plusOne(self, digits):
def countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob):
    arriveAlice = '2023-' + arriveAlice
    leaveAlice = '2023-' + leaveAlice
    arriveBob = '2023-' + arriveBob
    leaveBob = '2023-' + leaveBob
    arriveAlice = datetime.strptime(arriveAlice, '%Y-%m-%d').date()
    leaveAlice = datetime.strptime(leaveAlice, '%Y-%m-%d').date()
    arriveBob = datetime.strptime(arriveBob, '%Y-%m-%d').date()
    leaveBob = datetime.strptime(leaveBob, '%Y-%m-%d').date()

    late_arrive = max(arriveAlice,arriveBob)
    early_leave = min(leaveAlice,leaveBob)
    #print(late_arrive,early_leave)
    overlap = (early_leave - late_arrive).days +1
    return max(0,overlap)





arriveAlice = "08-15"
leaveAlice = "08-18"
arriveBob = "08-16"
leaveBob = "08-19"
print(countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob))

