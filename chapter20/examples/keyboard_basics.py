import pyautogui

# Sending strings from the keyboard
pyautogui.click(500, 500)
pyautogui.write('Hello, world!')

# Using key names instead of strings
pyautogui.write(['enter', 'a', 'b', 'left', 'left', 'X', 'Y'])

# The kotkey method makes automation life easier
pyautogui.hotkey('ctrl', 'a')
