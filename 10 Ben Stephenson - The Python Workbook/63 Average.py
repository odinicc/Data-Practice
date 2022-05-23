from statistics import mean

# Read the first value from the user
x = int(input("Enter an integer (0 to quit): "))
i =[]
# Keep looping while the user enters a non-zero number
while x != 0:
# Append number
    i.append(x)
# Read the next value from the user
    x = int(input("Enter an integer (0 to quit): "))
print("average value", mean(i))
