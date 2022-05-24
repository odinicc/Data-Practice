#Imagine you're writing an exercise-tracking app like Fitbit
#or MyFitnessPal. Part of your app is that a user can log an
#exercise session by naming the exercise, the intensity, and
#the duration.
#
#Write a class called ExerciseSession. ExerciseSession
#should have a constructor that requires two strings and an
#integer: the strings represent the exercise name and the
#exercise intensity, which will be "Low", "Moderate", or
#"High". The integer will represent the length of the
#exercise session in minutes. These should be saved in the
#instance of the class.

class ExerciseSession:
    def __init__(self, exercise_name, exercise_intensity,ex_session ):
        self.exercise_name = exercise_name
        self.exercise_intensity = exercise_intensity
        self.ex_session = ex_session
#
#Then, add three getters to the class. The getters should
#be named get_exercise, get_intensity, and get_duration,
#and should return the exercise string, the exercise
#intensity, and the duration, respectively.
#
    def get_exercise(self):
        return self.exercise_name

    def get_intensity(self):
        return self.exercise_intensity

    def get_duration(self):
        return self.ex_session


#The setters should be named set_exercise, set_intensity,
#and set_duration. Each should have one parameter (besides
#self), which should be stored as the new value of
#exercise, intensity, or duration. You may assume only
#valid values will be passed in.
#
    def set_exercise(self,exercise_name):
        self.exercise_name = exercise_name

    def set_intensity(self,exercise_intensity):
        if exercise_intensity not in ["Low", "Moderate","High"]:
            print("exercise_intensity should be Low, Moderate or High")
            return -1
        self.exercise_intensity = exercise_intensity
        return 1

    def set_duration(self, ex_session ):
        ex_session = str(ex_session)
        if ex_session.isdigit():
            self.ex_session = ex_session
        else:
            print("ex_session should be int")
#Add a new method to that class called calories_burned.
#calories_burned should have no parameters (besides self, as
#every method in a class has). It should return an integer
#representing the number of calories burned according to the
#following formula:
#
# - If the intensity is "Low", 4 calories are burned per
#   minute.
# - If the intensity is "Medium", 8 calories are burned
#   per minute.
# - If the intensity is "High", 12 calories are burned per
#   minute.


    def calories_burned(self):
        if self.exercise_intensity == "Low":
            return 4 * int(self.ex_session)
        elif self.exercise_intensity == "Moderate":
            return 8 * int(self.ex_session)
        elif self.exercise_intensity == "High":
            return 12 * int(self.ex_session)
        else:
            print("Error can't recognise exercise_intensity in ")

#If your code is implemented correctly, the lines below
#will run error-free. They will result in the following
#output to the console:
#Running
#Low
#60
#Swimming
#High
#30
'''
new_exercise = ExerciseSession("Running", "Low", 60)
print(new_exercise.get_exercise())
print(new_exercise.get_intensity())
print(new_exercise.get_duration())
new_exercise.set_exercise("Swimming")
new_exercise.set_intensity("High")
new_exercise.set_duration(30)
print(new_exercise.get_exercise())
print(new_exercise.get_intensity())
print(new_exercise.get_duration())
'''

#If your code is implemented correctly, the lines below
#will run error-free. They will result in the following
#output to the console:
#240
#360
new_exercise = ExerciseSession("Running", "Low", 60)
print(new_exercise.calories_burned())
new_exercise.set_exercise("Swimming")
new_exercise.set_intensity("High")
new_exercise.set_duration(30)
print(new_exercise.calories_burned())

