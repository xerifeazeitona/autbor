"""
Beautiful Soup is a module for extracting information from an HTML page
(and is much better for this purpose than regular expressions).
"""

import requests
import bs4

# Creating a BeautifulSoup Object from an internet HTML
res = requests.get('https://nostarch.com')
res.raise_for_status()
no_starch_soup = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(no_starch_soup))

# Creating a BeautifulSoup Object from a local HTML file
with open('example.html') as file_obj:
    example_soup = bs4.BeautifulSoup(file_obj, 'html.parser')
print(type(no_starch_soup))

# Once you have a BeautifulSoup object, you can use its methods to
# locate specific parts of an HTML document:

# experimenting with all elements with id="author"
elems = example_soup.select('#author')
print(type(elems))
print(len(elems))
print(type(elems[0]))
print(str(elems[0])) # The Tag object as a string
print(elems[0].getText())
print(elems[0].attrs)

# experimenting with all the <p> elements
p_elems = example_soup.select('p')
print('p_elems[0]:')
print(str(p_elems[0]))
print(p_elems[0].getText())
print('p_elems[1]:')
print(str(p_elems[1]))
print(p_elems[1].getText())
print('p_elems[2]:')
print(str(p_elems[2]))
print(p_elems[2].getText())
print()

# The get() method for Tag objects makes it simple to access attribute
# values from an element.
span_elem = example_soup.select('span')[0]
print(str(span_elem))
print(span_elem.get('id'))
print(span_elem.get('nonexistent_addr') is None)
print(span_elem.attrs)
