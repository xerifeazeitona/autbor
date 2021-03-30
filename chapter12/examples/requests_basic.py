"""
The requests module lets you easily download files from the web without
having to worry about complicated issues such as network errors,
connection problems, and data compression.
"""

import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(f'the requests.get() returns a {type(res)} object')
if res.status_code == requests.codes.ok:
    print('the requested file was downloaded successfully')
print(f'the requested file has {len(res.text)} words in it.')
print("\nHere's a small sample:")
print(res.text[:250])

# The raise_for_status() method is a good way to ensure that a program
# halts if a bad download occurs.
print('\n\nPreparing a bad request...')
res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f'There was a problem: {err}')

# To write the web page to a ﬁle, you can use a for loop with the
# Response object’s iter_content() method.
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
try:
    res.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f'There was a problem: {err}')
with open('RomeoAndJuliet.txt', 'wb') as file_obj:
    for chunk in res.iter_content(100000):
        file_obj.write(chunk)
