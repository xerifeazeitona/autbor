#! /usr/bin/env python3
"""
Extending the Multi-Clipboard
Extend the multi-clipboard program in this chapter so that it has a
delete <keyword> command line argument that will delete a keyword from
the shelf. Then add a `delete` command line argument that will delete
all keywords.
"""

import sys
import shelve
import pyperclip

usage = '''
mcb.pyw - Saves and loads pieces of text to the clipboard.

Usage:  ./mcb.pyw save <keyword> - Saves clipboard to keyword.
		./mcb.pyw <keyword> - Loads keyword to clipboard.
		./mcb.pyw list - Loads all keywords to clipboard.
		./mcb.pyw delete <keyword> - Delete keyword from the database.
		./mcb.pyw delete - Delete all keywords from the database.
'''

mcb_shelf = shelve.open('mcb')

if len(sys.argv) == 3:
    # Save Clipboard content
    if sys.argv[1].lower() == 'save':
        mcb_shelf[sys.argv[2]] = pyperclip.paste()
        print(f"'{sys.argv[2]}' saved to the keyword database.\n")
    # Delete keyword from database
    elif sys.argv[1].lower() == 'delete':
        del mcb_shelf[sys.argv[2]]
        print(f"'{sys.argv[2]}' removed from the keyword database.\n")
    else:
        print(usage)
elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
        print("Stored keywords: " + str(list(mcb_shelf.keys())))
    # Delete all stored keywords
    elif sys.argv[1].lower() == 'delete':
        for key in mcb_shelf.keys():
            del mcb_shelf[key]
        print("All keys removed from the keyword database.\n")
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])
    else:
        print(usage)
else:
    print(usage)

mcb_shelf.close()
