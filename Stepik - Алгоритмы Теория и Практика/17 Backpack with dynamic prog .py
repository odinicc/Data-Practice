import random
import sys

def read_data():
    #for local solution
    inf = open('1.txt', 'r')

    #for system solution
    # inf = sys.stdin

    Lines = inf.readlines()

    First_Line = Lines[0]
    words = First_Line.split(" ")
    back_pack = int(words[1].replace('\n', ''))
    n = int(words[0])
    Lines.pop(0)

goods = []

