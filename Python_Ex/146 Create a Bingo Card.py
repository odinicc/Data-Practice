import random
import pprint

def create_card():
    bingo = list("BINGO")
    b = {}
    for i in range(len(bingo)):
        p = []
        for l in range(5):
            num = random.randint(i*15, (i+1)*15)
            p.append(num)
        b[bingo[i]] = p
    return b

def displayCard(card):
    # Display the headings
    print(" B     I     N     G    O")
    # Display the numbers on the card
    for i in range(5):
        for letter in ["B", "I", "N", "G", "O"]:
            print("%2d   " % card[letter][i], end="")
        print()



b = create_card()
displayCard(b)

