import portion as p
from datetime import datetime, timedelta
import math

start_datestr = '2024-05-07 15:20:00'
end_datestr='2024-05-08 22:30:00'

date_format = "%Y-%m-%d %H:%M:%S"

night_interval=p.Interval()
#print(f'Night Interval : {night_interval}')

start_date = datetime.strptime(start_datestr, date_format)
#print(f'Start Date : {start_date}')

end_date = datetime.strptime(end_datestr, date_format)
#print(f'End Date : {end_date}')

keep_intervals = p.closed(start_date, end_date) 
#print(f'Interval : {keep_intervals}')

for _ in range(start_date.day,end_date.day+1):
    interval_start = start_date.replace(hour=0, minute=0, second=0, microsecond=0)
    interval_end = start_date.replace(hour=6, minute=0, second=0, microsecond=0)
    night_interval = night_interval.union(p.closed(interval_start, interval_end))
    start_date += timedelta(days=1)
#print(night_interval)

hours=timedelta(0)
print(hours)
for i in keep_intervals - night_interval:
    #print(i)
    hours += (i.upper - i.lower)
    
hours = hours.days * 24 + hours.seconds / 3600

print("\nResult After Removing Night Interval (12 AM to 6 AM) From Two Dates : ", (str(math.floor(hours))+' Hours\n'))
