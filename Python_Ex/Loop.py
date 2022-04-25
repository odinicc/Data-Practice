# Read the first value from the user
x = int(input("Enter an integer (0 to quit): "))
# Keep looping while the user enters a non-zero number
while x != 0:
# Report the nature of the number
    if x > 0:
        print("That’s a positive number.")
    else:
        print("That’s a negative number.")
# Read the next value from the user
    x = int(input("Enter an integer (0 to quit): "))
