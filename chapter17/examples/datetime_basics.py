"""
The time module is useful for getting a Unix epoch timestamp to work
with. But if you want to display a date in a more convenient format, or
do arithmetic with dates, you should use the datetime module.
"""
import datetime
import time

# datetime values represent a specific moment in time
print(datetime.datetime.now())
dt = datetime.datetime(2020, 10, 21, 16, 29, 0)
print(f'{dt.year, dt.month, dt.day}')
print(f'{dt.hour, dt.minute, dt.second}')

# The fromtimestamp() function converts a unix epoch timestamp to a
# datetime object
print(datetime.datetime.fromtimestamp(1000000))
print(datetime.datetime.fromtimestamp(time.time()))

# You can use comparison operators with datetime objects
halloween2020 = datetime.datetime(2020, 10, 31, 0, 0, 0)
newyears2021 = datetime.datetime(2021, 1, 1, 0, 0, 0)
oct31_2020 = datetime.datetime(2020, 10, 31, 0, 0, 0)
print(halloween2020 == oct31_2020)
print(halloween2020 > newyears2021)
print(newyears2021 > halloween2020)
print(newyears2021 != oct31_2020)

# The timedelta type represents a duration of time, rather than a moment
delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(f'{delta.days, delta.seconds, delta.microseconds}')
print(delta.total_seconds())
print(delta)

# The arithmetic operators can be used to perform date arithmetic
dt = datetime.datetime.now()
print(dt)
thousand_days = datetime.timedelta(days=1000)
print(dt + thousand_days)
oct21st = datetime.datetime(2020, 10, 21, 16, 29, 0)
about_thirty_years = datetime.timedelta(days=365*30)
print(oct21st)
print(oct21st - about_thirty_years)
print(oct21st - (2 * about_thirty_years))

# You can use the time.sleep() function to pause a program until a date
halloween2016 = datetime.datetime(2016, 10, 31, 0, 0, 0)
while datetime.datetime.now() < halloween2016:
    time.sleep(1)

# Use the strftime() method to display a datetime object as a string
print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))
print(oct21st.strftime('%I:%M %p'))
print(oct21st.strftime("%B of '%y"))
