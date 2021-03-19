#! /usr/bin/env python3
"""
mclip.py - A multi-clipboard program
"""

import sys
import pyperclip

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
		'busy': """Sorry, can we do this later this week or next week?""",
		'upsell': """Would you consider making this a monthly donation?"""}

# If no argument was provided, print usage
if len(sys.argv) < 2:
    print('Usage: mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f'Text for {keyphrase} copied to the clipboard.')
else:
    print(f'There is no stored text for {keyphrase}.')
