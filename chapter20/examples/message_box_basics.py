import pyautogui

# alert returns 'OK'
pyautogui.alert('This is a message', 'Important')

# confirm returns 'OK' or 'Cancel'
pyautogui.confirm('Do you want to continue?')

# prompt returns what the user entered
pyautogui.prompt("What is your cat's name?")

# password is the same as prompt, but hides the input with asterisks
pyautogui.password('What is the password?')
