import time
import datetime as dt


'''
print('we`re waiting for something')
time.sleep(3)
print('we`re finished waiting')
'''
today = dt.date(year=2023, month=10, day=19)
print(dt.time(hour=12))
real_now = dt.datetime.now()
super_real_now = dt.datetime.now()

in_a_week = dt.date(year=2023, month=10,day=26)
resulting_week = in_a_week - today
print(type(resulting_week))
print(in_a_week + resulting_week)
datetime_now_example = dt.datetime(year=2012,month=9,day=15, hour=12,minute=12,second=12,microsecond=12)
print(datetime_now_example)
long_time_ago = real_now-datetime_now_example
print(real_now <= super_real_now)
print(real_now >= datetime_now_example)
print(long_time_ago + resulting_week)
timestamp_example = dt.datetime.timestamp(datetime_now_example)
print(timestamp_example)
timestamp_example +=86400
come_back_to_normal_time = dt.datetime.fromtimestamp(timestamp_example)
print(come_back_to_normal_time)
formatted_time = dt.datetime.strptime('2023-19-10 20:11:11', '%Y-%d-%m %H:%M:%S')
print(formatted_time)
cur_date = formatted_time.strftime("%d/%m/%Y, %H:%M:%S")
print(cur_date)
print(type(cur_date))

