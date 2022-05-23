class Student:
    def __init__(self):
        self.studentName = ""
        self.GPA = 0.0
        self.creditHours = 0
        self.enrolled = True
        self.classes = []

newStudent  = Student()
newStudent.enrolled = True
newStudent.GPA = 3.9
newStudent.creditHours = 1334
newStudent.classes = ["CS1301", "PHYS3001", "ISYE3029"]
