import re

def detectCapitalUse(word):
    if len(word) == 0:
        return True

    if word[0].isupper():
        first_let = 'Big'
    else:
        first_let = 'Small'

    if bool(re.search(r"^[A-Z]+$", word)):
        all__other_let = 'Big'
    elif bool(re.search(r"^[a-z]+$", word)):
        all__other_let = 'Small'
    else:
        return False
    print(first_let,all__other_let)
    if first_let == 'Small' and all__other_let == 'Big':
        return False
    else:
        return True

word = "Usa"
print(detectCapitalUse(word))

