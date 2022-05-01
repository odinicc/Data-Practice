from random import randrange
import pprint

def Two_Dice_Simulation():
    overal = {}
    ran = 10000
    for i in range(ran):
        x = randrange(1,7)
        y = randrange(1,7)
        z = x + y
        if z in overal:
            overal[z] += 1/ran
        else:
            overal[z] = 1/ran
    return overal


p = Two_Dice_Simulation()
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(p)
