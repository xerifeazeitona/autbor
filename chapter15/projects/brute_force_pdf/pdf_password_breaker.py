"""
Brute-Force PDF Password Breaker
Say you have an encrypted PDF that you have forgotten the password to,
but you remember it was a single English word. Trying to guess your
forgotten password is quite a boring task.
Instead you can write a program that will decrypt the PDF by trying
every possible English word until it finds one that works.

The text file dictionary.txt contains over 44,000 English words. Using
the file-reading skills you learned in Chapter 9, create a list of word
strings by reading this file.
Then loop over each word in this list, passing it to the decrypt()
method.
If this method returns the integer 0, the password was wrong and your
program should continue to the next password.
If decrypt() returns 1, then your program should break out of the loop
and print the hacked password.
You should try both the uppercase and lowercase form of each word.
"""

import sys
import PyPDF2

# Open PDF file
pdf_reader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))

# Read dictionary words from text file
with open('dictionary.txt') as file_object:
    wordlist = file_object.read().split('\n')

# try to brute-force the password
total_words = len(wordlist)
for i, word in enumerate(wordlist):
    print(f'\r{i} / {total_words}', end='')
    if pdf_reader.decrypt(word) == 1:
        print(f'\nPassword found: "{word}"')
        sys.exit()
    if pdf_reader.decrypt(word.lower()) == 1:
        print(f'\nPassword found: "{word.lower()}"')
        sys.exit()

print('\nCould not find a valid password.')
