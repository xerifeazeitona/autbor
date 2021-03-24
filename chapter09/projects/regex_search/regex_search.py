"""
Regex Search

Write a program that opens all *.txt* ﬁles in a folder and searches for
any line that matches a user-supplied regular expression.
The results should be printed to the screen.
"""

import re
from pathlib import Path

# opens all txt files in a folder
def read_file(filename):
    """Return the contents of file as a string."""
    with open(filename) as file_object:
        return file_object.readlines()

def get_txt_files(folder):
    """Returns a list with all text files inside the provided folder."""
    txt_files = []
    path_obj = Path(folder)
    for txt_file in path_obj.glob('*.txt'):
        txt_files.append(str(txt_file))
    return txt_files

def get_user_regex():
    """Returns a Regex object complied with the user input."""
    user_input = input('Enter a regex for the search: ')
    return re.compile(user_input)

def perform_search(folder):
    """Main function that does all the magic"""
    user_regex = get_user_regex()
    txt_files = get_txt_files(folder)
    for txt_file in txt_files:
        print(f'\nScanning {Path(txt_file).name}...')
        content = read_file(txt_file)
        for line in content:
            matched = user_regex.findall(line)
            if matched:
                print(line)
    print('...done!')

perform_search(Path.cwd())
