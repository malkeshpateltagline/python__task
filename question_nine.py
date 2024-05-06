from portion import closed
from datetime import datetime

start_datestr = '2024-05-07 1'
end_datestr='2024-05-08 22'

date_format = "%Y-%m-%d %H"

start_date = datetime.strptime(start_datestr, date_format)
end_date = datetime.strptime(end_datestr, date_format)

keep_intervals = closed(start_date.hour, end_date.hour) 
#print(keep_intervals)
day_difference = (end_date - start_date).days
#print(day_difference)

day_difference=day_difference*18
hours=0

for i in range(keep_intervals.lower,keep_intervals.upper):
    hours+=1

#print(hours)
print("\nResult After Removing Night Interval (12 AM to 6 AM) From Two Dates : ", (str(hours+day_difference)+' Hours\n'))