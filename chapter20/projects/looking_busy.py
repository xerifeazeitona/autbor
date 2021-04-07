"""
Looking Busy

Many instant messaging programs determine whether you are idle, or away
from your computer, by detecting a lack of mouse movement over some
period of time—say, 10 minutes. Maybe you’re away from your computer but
don’t want others to see your instant messenger status go into idle mode.

Write a script to nudge your mouse cursor slightly every 10 seconds.
The nudge should be small and infrequent enough so that it won’t get in
the way if you do happen to need to use your computer while the script
is running.
"""

import sys
from random import randint
import pyautogui

direction = 1

try:
    while True:
        x = randint(5, 10) * direction
        y = randint(5, 10) * direction
        pyautogui.PAUSE = 10
        pyautogui.move(x, y)
        direction *= -1
except KeyboardInterrupt:
    sys.exit()
