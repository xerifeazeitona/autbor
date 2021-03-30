#! /usr/bin/env python3
"""
download_xkcd.py - Downloads every single XKCD comic.
"""

import os
import requests
import bs4

url = 'https://xkcd.com'            # starting url
os.makedirs('xkcd', exist_ok=True)  # store downloaded comics in ./xkcd
while not url.endswith('#'):
    # Download the page
    print(f'Downloading page {url}...')
    res = requests.get(url)
    res.raise_for_status()

    soup_obj = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the URL of the comic image
    comic_element = soup_obj.select('#comic img')
    if not comic_element:
        print('Could not find comic image.')
    else:
        comic_url = f"https:{comic_element[0].get('src')}"
        res = requests.get(comic_url)
        res.raise_for_status()

    # Save the image to ./xkcd
    with open(
        os.path.join('xkcd', os.path.basename(comic_url)),
        'wb') as file_obj:
        for chunk in res.iter_content(100000):
            file_obj.write(chunk)

    # Get the Prev button's url
    prev_link = soup_obj.select('a[rel="prev"]')[0]
    url = f"https://xkcd.com{prev_link.get('href')}"

print('Done.')