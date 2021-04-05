#! /usr/bin/env python3
"""
countdown.py - A simple countdown script
"""

import time
import subprocess

time_left = 5
while time_left > 0:
    print(time_left, end='\r')
    time.sleep(1)
    time_left -= 1

# At the end of countdown, play a sound file
subprocess.Popen(['mpv', 'alarm.wav']).wait()
