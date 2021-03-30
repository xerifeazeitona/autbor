#! /usr/bin/env python3
"""
search_pypi.py - Opens several search results.
"""

import sys
import webbrowser
import requests
import bs4

print('Searching...') # display text while downloading the search result page
res = requests.get('https://pypi.org/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links
soup_obj = bs4.BeautifulSoup(res.text, 'html.parser')
# Open a browser tab for each result
link_elements = soup_obj.select('.package-snippet')
num_open = min(5, len(link_elements))
for i in range(num_open):
    url_to_open = f"https://pypi.org{link_elements[i].get('href')}"
    print(f'Opening {url_to_open}...')
    webbrowser.open(url_to_open)
