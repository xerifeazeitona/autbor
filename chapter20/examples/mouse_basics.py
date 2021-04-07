import pyautogui

# Before playing with the mouse is good to know your limits
wh = pyautogui.size() # obtain screen resolution
print(wh)

# Scrolling the mouse
pyautogui.scroll(200)

# moveTo() will move the cursor to a specified position on the screen
for i in range(2):
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)

# move() will move the cursor relative to its current position
for i in range(2):
    pyautogui.move(100, 0, duration=0.25)   # right
    pyautogui.move(0, 100, duration=0.25)   # down
    pyautogui.move(-100, 0, duration=0.25)  # left
    pyautogui.move(0, -100, duration=0.25)  # up

# Getting the mouse position
print(pyautogui.position())
p = pyautogui.position()
print(p)
print(p[0]) # The x-coordinate is at index 0
print(p.x)  # The x-coordinate is also in the 'x' attribute

# Clicking the mouse
pyautogui.click(25, 270) # Move the mouse to (25, 270) and click

# Dragging the mouse (Check spiral_draw.py)
