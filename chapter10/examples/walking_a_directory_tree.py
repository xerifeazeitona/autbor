"""
The os.walk() function is passed a single string value: a folder path.
You can use os.walk() in a for loop statement to walk a directory tree,
much like how you can use the range() function to walk over a range of
numbers. Unlike range(), the os.walk() function will return three values
on each iteration through the loop:

- A string of the current folder’s name
- A list of strings of the folders in the current folder
- A list of strings of the ﬁles in the current folder

Since os.walk() returns lists of strings for the subfolder and filename
variables, you can use these lists in their own for loops.  
"""

import os

for folder_name, subfolders, filenames in os.walk('/home/korporal/labs'):
    print(f'The current folder is {folder_name}')

    for subfolder in subfolders:
        print(f'Subfolder of {folder_name}: {subfolder}')

    for filename in filenames:
        print(f'File inside {folder_name}: {filename}')

print()
