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

def generate_numbers(n):
    ren = list(range(1,76))
    l = []
    for i in range(n):
        m = random.choice(ren)
        n = ren.pop(m)
        l.append(n)
    return l

def match_numbers(card, l ):
    for i in range(len(card)):
        return
    
    



b = create_card()
displayCard(b)
l = generate_numbers(5)

print(l)
print(b)
