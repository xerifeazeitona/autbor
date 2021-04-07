#! /usr/bin/env python3
"""
form_filler.py - Automatically fills in the form
"""

import time
import pyautogui

# Set this to the correct coordinates for your computer
submit_another_link = (750, 265)

form_data = [
    {'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
    'robocop': 4, 'comments': 'Tell Bob I said hi.'},
    {'name': 'Bob', 'fear': 'bees', 'source': 'amulet','robocop': 4,
    'comments': 'n/a'},
    {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
    'robocop': 1,
    'comments': 'Please take the puppets out of the break room.'},
    {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money', 'robocop': 5,
    'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
    {'name': 'Anne Lewis', 'fear': 'McDaggett', 'source': 'money',
    'robocop': 5, 'comments': 'Murphy? Is that you?!'},
    ]

pyautogui.PAUSE = 0.5
print('Ensure that the browser window is active and the form is loaded!')

for person in form_data:
    # Give the user a chance to kill the script
    print('>>> 5-SECOND PAUSE TO LET USERS PRESS CTRL-C <<<')
    time.sleep(5)

    print(f"Entering {person['name']} info...")
    pyautogui.write(['tab', 'tab'])

    # Fill out the name field
    pyautogui.write(person['name'] + '\t')

    # Fill out the fear field
    pyautogui.write(person['fear'] + '\t')

    # Fill out the source of power field
    if person['source'] == 'wand':
        pyautogui.write(['down', 'enter', 'tab'], 0.5)
    elif person['source'] == 'amulet':
        pyautogui.write(['down', 'down', 'enter', 'tab'], 0.5)
    elif person['source'] == 'crystal ball':
        pyautogui.write(['down', 'down', 'down', 'enter', 'tab'], 0.5)
    elif person['source'] == 'money':
        pyautogui.write(['down', 'down', 'down', 'down', 'enter', 'tab'], 0.5)

    # Fill out the RoboCop field
    if person['robocop'] == 1:
        pyautogui.write([' ', 'tab', 'tab'], 0.5)
    elif person['robocop'] == 2:
        pyautogui.write(['right', 'tab', 'tab'], 0.5)
    elif person['robocop'] == 3:
        pyautogui.write(['right', 'right', 'tab', 'tab'], 0.5)
    elif person['robocop'] == 4:
        pyautogui.write(['right', 'right', 'right', 'tab', 'tab'], 0.5)
    elif person['robocop'] == 5:
        pyautogui.write(['right', 'right', 'right', 'right', 'tab', 'tab'], 0.5)

    # Fill the additional comments field
    pyautogui.write(person['comments'] + '\t')

    # Click submit button
    time.sleep(0.5) # Wait for the button to activate
    pyautogui.press('enter')

    # Wait until form page has laded
    print('Submitted form.')
    time.sleep(5)

    # Click the Submit another response link
    pyautogui.click(submit_another_link[0], submit_another_link[1])
