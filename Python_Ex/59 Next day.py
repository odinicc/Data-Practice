
from datetime import datetime as dt
import datetime

date_time_str = '04-09-19'
date_time_obj = dt.strptime(date_time_str, '%d-%m-%y')
date_time_obj  =  date_time_obj + datetime.timedelta(days=1)

print('date_time_obj = ' , date_time_obj)


#a = input("Give me the the date ")


