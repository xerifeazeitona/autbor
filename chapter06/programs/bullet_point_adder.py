#! /usr/bin/env python3
"""
bullet_point_adder.py - Adds Wikipedia bullet point to the start of each
line of text on the clipboard.
"""

import pyperclip

# Separate lines and add stars
lines = pyperclip.paste().split('\n')

for i, _ in enumerate(lines): # Loop through all indexes in the list
    lines[i] = '* ' + lines[i] # add star to each string in the list

pyperclip.copy('\n'.join(lines))
