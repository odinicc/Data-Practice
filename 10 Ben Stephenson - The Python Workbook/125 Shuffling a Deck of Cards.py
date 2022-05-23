import random

def createDeck():
    characters = list(range(2, 10))
    characters_2 = ['T','J','Q','K','A']
    suit = ['s','h','d','c']
    cards = []

    #Create cards with numbers like 9s
    for s in suit:
        for c in characters:
            card =  str(c) + str(s) 
            cards.append(card)

    #Create cards with letters like Td
    for s in suit:
        for c in characters_2:
            card = str(c) + str(s) 
            cards.append(card)
            
    return cards

def shuffle(cards):
   cards_random =  random.sample(cards , len(cards))
   return cards_random

def deal(cards_random , num_cards , num_hands):
    xi = {}
    for j  in range(num_hands):
        fi =[]
        for i  in range(num_cards):
            fi.append(cards_random.pop(2))
        print('fi = '  , fi)
        print("cards_random = ", cards_random)
        xi[j] = fi
    print('xi = '  , xi)

cards = createDeck()
print("cards = ", cards)

cards_random = shuffle(cards)

print("cards_random = ", cards_random)

deal(cards_random,3,7)

