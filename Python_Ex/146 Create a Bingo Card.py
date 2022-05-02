import random
import pprint

#Function to generate card
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

#Function to display card
def displayCard(card):
    # Display the headings
    print(" B     I     N     G    O")
    # Display the numbers on the card
    for i in range(5):
        for letter in ["B", "I", "N", "G", "O"]:
            print("%2d   " % card[letter][i], end="")
        print()

#Function that generate numbers for lists
def generate_numbers(n):
    ren = list(range(1,76))
    l = []
    for i in range(n):
        m = random.choice(ren)
        ren.remove(m)
        l.append(m)
    return l

#Function that replace list numbers in card with 0 
def match_numbers(card, l ):
    for key in card:
        k = len(card[key])
        for j in  range(k):
            m = card[key][j]
            if m in l:
                card[key][j] = 0
    return card
            
#Function that take card with 0 and give back the result is it wining card or not 
def is_wining(card):
    it = 0
    diag1 = []
    diag2 = []
    for key in card:
        k = len(card[key])
        m = []
        for j in range(k):
            #Check if row contain all 0
            if card[key][j] != 0:
                break
            if j == k-1:
                return True
            #Check if column contain all 0
            if card[key][j] == 0:
                m.append(card[key][j])
            if len(m) == k:
                return True
        #Check if diagonal 1 contain all 0
        if card[key][it] == 0:
            diag1.append(card[key][it])
        if len(diag1) == k:
            return True
        
        #Check if diagonal 2 contain all 0
        if card[key][k-it-1] == 0:
            diag2.append(card[key][k-it-1])
        if len(diag2) == k:
            return True
        
        it += 1
    return False      
                
def play_bingo(games, numbers):
    win = 0
    for i in range(games):
        l = generate_numbers(numbers)
        card = create_card()
        card2 = match_numbers(card, l )
        if ( is_wining(card2) == True ):
            win += 1
    overal = win / games
    return overal

b = create_card()
displayCard(b)
l = generate_numbers(35)
print("l = ", l)
card2 = match_numbers(b, l )
displayCard(card2)
print("Card is wining ", is_wining(card2))

games = 1000
numbers = 65

print ("play_bingo( games = ", games,", numbers =",numbers, ") = ",play_bingo(games, numbers))
