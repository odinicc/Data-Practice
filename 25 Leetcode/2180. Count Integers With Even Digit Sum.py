import math
from datetime import datetime


def dayOfTheWeek(day, month, year):
    dayt = datetime(year, month, day )
    return  dayt.strftime("%A")

print(dayOfTheWeek(29,12,2021))