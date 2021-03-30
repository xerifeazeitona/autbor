"""
Link Verification
Write a program that, given the URL of a web page, will attempt to
download every linked page on the page.
The program should flag any pages that have a 404 “Not Found” status
code and print them out as broken links.
"""

import requests
import bs4

# Creating a BeautifulSoup Object from an internet HTML
res = requests.get('https://puppylinux.com/faq.html')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# experimenting with all a elements
elems = soup.select('a')
print(f'found {len(elems)} elements')
for i, _ in enumerate(elems):
    try:
        temp_res = requests.get(elems[i].attrs.get('href', ''))
        temp_res.raise_for_status()
    except requests.exceptions.MissingSchema as err:
        print(err)
    except requests.exceptions.HTTPError as err:
        print(err)
