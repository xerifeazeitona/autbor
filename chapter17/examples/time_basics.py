import time

# The time.time() function returns the number of seconds since Unix epoch
print(time.time())

# The time.ctime() function returns a string description of current time
print(time.ctime())
# You can also pass the number of seconds since Unix epoch
this_moment = time.time()
print(time.ctime(this_moment))

# If you need to pause your program, call time.sleep()
for i in range(3):
    print('Tick')
    time.sleep(1)
    print('Tock')
    time.sleep(1)

# Since time often returns floats with many digits, use the round()
# function for better readability
now = time.time()
print(now)
print(round(now, 2))
print(round(now, 4))
print(round(now))
