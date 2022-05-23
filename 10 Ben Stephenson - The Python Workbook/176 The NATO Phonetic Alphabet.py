import pprint

Nato = {
    'A':'Alpha',
    'B':'Bravo',
    'C':'Charlie',
    'D':'Delta',
    'E':'Echo',
    'F':'Foxtrot',
    'G':'Golf',
    'H':'Hotel',
    'I':'India',
    'J':'Juliett',
    'K':'Kilo',
    'L':'Lima',
    'M':'Mike',
    'N':'November',
    'O':'Oscar',
    'P':'Papa',
    'Q':'Quebec',
    'R':'Romeo',
    'S':'Sierra',
    'T':'Tango',
    'U':'Uniform',
    'V':'Victor',
    'W':'Whiskey',
    'X':'X-ray',
    'Y':'Yankee',
    'Z':'Zulu',
    ' ':' ',
}

def Nato_f(string):
    l = len(string)
    if l == 0:
        return
    temp = string[l-1]
    Nato_f(string[:l-1])
    temp = temp.upper()
    try:
        print(Nato[temp],' ' , end='')
    except:
        pass

# Driver program to test above function
string = "Geeks for - Geeks"
Nato_f(string)