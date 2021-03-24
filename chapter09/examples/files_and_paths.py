"""
All those examples were designed to run on the interpreter, not a py file
"""

import os
from pathlib import Path

# You can create path objects with the Path method
Path('spam', 'bacon', 'eggs')
str(Path('spam', 'bacon', 'eggs'))

# Using the / Operator to Join Paths
# All 3 examples lead to the same result
Path('spam') / 'bacon' / 'eggs'
Path('spam') / Path('bacon/eggs')
Path('spam') / Path('bacon', 'eggs')

# To obtain the current working directory
Path.cwd()

# To change the current working directory
os.chdir('/usr/share/doc/')
Path.cwd()

# To get the home directory
Path.home()

# To create new folders, you can use os.makedirs or Path().mkdir()
os.makedirs(Path.home() / 'delicious/walnut/waffles')
Path(r'/tmp/spam').mkdir()

# Get parts of a file path
p = Path('/usr/share/doc/nano/faq.html')
p.anchor    # root folder 
p.parent    # the folder that contains the file
p.name      # entire filename
p.stem      # just the filename
p.suffix    # just the file extension
p.drive     # Windows only, shows the drive letter

# Get the size of a file
os.path.getsize('/etc/os-release')

# list all files in a directory
os.listdir('/etc')

# using the two methods above, you can get the total size of a directory
total_size = 0
for filename in os.listdir('/etc'):
    total_size += os.path.getsize(os.path.join('/etc', filename))
print(total_size)

# Path objects have a glob() method for listing contents of a folder
# according to a glob pattern
p = Path('/etc')
p.glob('*')             # return a generator object
list(p.glob('*'))       # Make a list from the generator object
list(p.glob('*.txt'))   # List all files with a .txt extension

# Checking path validity
p.exists()  # check if the path exists
p.is_dir()  # check if the path is a directory (False for files)
p.is_file() # check if the path is a file (False for directories)