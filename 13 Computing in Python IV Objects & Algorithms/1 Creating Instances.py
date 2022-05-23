# Define the class Person
class Person:
    # Create a new instance of Person
    def __init__(self):
        # Person's default values
        self.firstname = "[no first name]"
        self.lastname = "[no last name]"
        self.eyecolor = "[no eye color]"
        self.age = -1

myperson = Person()
myperson.firstname = "Ivan"

print(myperson.firstname)
print(myperson.lastname)
print(myperson.eyecolor)
print(myperson.age)