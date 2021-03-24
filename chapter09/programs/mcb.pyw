#! /usr/bin/env python3
"""
mcb.pyw - Saves and loads pieces of text to the clipboard.

Usage:  ./mcb.pyw save <keyword> - Saves clipboard to keyword.
		./mcb.pyw <keyword> - Loads keyword to clipboard.
		./mcb.pyw list - Loads all keywords to clipboard.
"""

import sys
import shelve
import pyperclip

mcb_shelf = shelve.open('mcb')

# Save Clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
        print(list(mcb_shelf.keys()))
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()
