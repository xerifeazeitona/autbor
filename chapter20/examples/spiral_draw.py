"""
To try this program, first open a graphics-drawing application such as
MS Paint on Windows, Paintbrush on macOS, or GNU Paint on Linux.
Then with the pencil or brush tool selected, put your mouse cursor over
the canvas.
"""
import time
import pyautogui
time.sleep(5)
pyautogui.click()   # Click to make the window active
distance = 300
change = 20
while distance > 0:
    pyautogui.drag(distance, 0, duration=0.2)   # move right
    distance -= change
    pyautogui.drag(0, distance, duration=0.2)   # move down
    pyautogui.drag(-distance, 0, duration=0.2)  # move left
    distance -= change
    pyautogui.drag(0, -distance, duration=0.2)  # move up
