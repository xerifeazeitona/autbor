"""
Regex Version of the strip() Method
Write a function that takes a string and does the same thing as the
strip() string method. 
"""

import re

def fake_strip(text, chars=' '):
    """
    Removes any leading and trailing characters. 
    If no other arguments are passed other than the string to strip,
    then whitespace characters will be removed from the beginning and
    end of the string.
    Otherwise, the characters speciﬁed in the second argument to the
    function will be removed from the string.
    """
    if chars == ' ':
        lead_regex = re.compile(r'^\s+')
        trail_regex = re.compile(r'\s+$')
    else:
        lead_regex = re.compile(f'^[{chars}]+')
        trail_regex = re.compile(f'[{chars}]+$')
    return trail_regex.sub('', lead_regex.sub('', text))

print(f"'{fake_strip('hello')}'")
print(f"'{fake_strip('            hello')}'")
print(f"'{fake_strip('hello           ')}'")
print(f"'{fake_strip('             hello     ')}'")
print(f"'{fake_strip('hello world')}'")
print(f"'{fake_strip('    hello world')}'")
print(f"'{fake_strip('hello world      ')}'")
print(f"'{fake_strip('ABChello worldABC', 'CBA')}'")
print(f"'{fake_strip('SpamSpamHelloSpamWorldSpam', 'ampS')}'")
