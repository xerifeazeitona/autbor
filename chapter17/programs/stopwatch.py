#! /usr/bin/env python3
"""
stopwatch.py - A simple stopwatch program
"""

import time

# Display instructions
usage_msg = 'Press ENTER to begin. '
usage_msg += 'Afterward, press ENTER to "click" the stopwatch. '
usage_msg += 'Press Ctrl-C to quit.'
input(usage_msg) # Press ENTER to begin
print('Started.')
start_time = time.time() # Get the first lap's start time
last_time = start_time
lap_num = 1

# Start tracking lap times
try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        print(f'Lap #{lap_num}: {total_time} ({lap_time})', end='')
        lap_num += 1
        last_time = time.time() # reset the last lap time
except KeyboardInterrupt:
    # Handle Ctrl-C exception to keep it's error message from displaying
    print('\nDone.')
    