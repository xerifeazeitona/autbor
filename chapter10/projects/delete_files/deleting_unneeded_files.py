"""
Deleting Unneeded Files

Write a program that walks through a folder tree and searches for
exceptionally large ﬁles or folders—say, ones that have a ﬁle size of
more than 100MB. (Remember that to get a ﬁle’s size, you can use
os.path.getsize() from the os module.)
Print these ﬁles with their absolute path to the screen.
"""

import os

def list_big_files(foldername, size):
    """Print the files in "foldername" that are larger than "size"(in MB)."""
    for folder, _, files in os.walk(foldername):
        print(f'\nChecking {os.path.basename(folder)}...')
        for filename in files:
            abs_name = os.path.abspath(os.path.join(folder, filename))
            file_size = os.path.getsize(abs_name)
            if file_size > size * 1048576:
                print(f'{abs_name} has a size of {round(file_size/1048576, 2)}MB')
    print('\n...done!')

example_folder = os.path.expanduser('~') + '/Downloads'
list_big_files(example_folder, 10)
