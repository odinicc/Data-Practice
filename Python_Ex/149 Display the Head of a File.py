import sys

inf = open("hamlet2.txt", 'r')

if len(sys.argv) < 3:
    print("You should run this script with arguments")
    quit()

arg1 = sys.argv[1]
arg2 = int(sys.argv[2])

Lines = inf.readlines()
if len(Lines) <= arg2:
    print('Argument 2 should be smaller then row numbers in file')
    quit()
if arg1 == 'head':
    print("type(Lines) = ", type(Lines))
    for i in range(arg2):
        #print("Lines[",i,"] = ", Lines[i])
        print(Lines[i], end='')

elif arg1 == 'tail':
    print("type(Lines) = ", type(Lines))
    for i in range(len(Lines) - arg2 , len(Lines)):
        print(Lines[i], end='')


else:
    print('Wrong paramter')