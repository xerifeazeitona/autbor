"""
ZipFile objects are conceptually similar to the File objects you saw
returned by the open() function in the previous chapter: they are values
through which the program interacts with the ﬁle. To create a ZipFile
object, call the zipfile.ZipFile() function, passing it a string of the
.ZIP ﬁle’s ﬁlename.
"""

import os
import zipfile
from pathlib import Path

p = Path.cwd()

# Creating ZIP files (if you omit arcname, it will add the absolute path
# to the compressed file)
example_zip = zipfile.ZipFile(p / 'example.zip', 'w')
example_zip.write(p / 'test.py', arcname='test.py', compress_type=zipfile.ZIP_DEFLATED)
example_zip.close()

# Adding to ZIP files
example_zip = zipfile.ZipFile(p / 'example.zip', 'a')
example_zip.write(p / 'lorem.txt', arcname='lorem.txt', compress_type=zipfile.ZIP_DEFLATED)
example_zip.close()

# Reading ZIP files
example_zip = zipfile.ZipFile(p / 'example.zip')
print(example_zip.namelist())
file_info = example_zip.getinfo('lorem.txt')
print(f'deflated size: {file_info.file_size}')
print(f'compressed size: {file_info.compress_size}')
print(f'Compressed file is {round(file_info.file_size / file_info.compress_size, 2)}x smaller!')
example_zip.close()

# Extracting from ZIP files
example_zip = zipfile.ZipFile(p / 'example.zip')
# Extract a single file (no second argument = extract on cwd)
example_zip.extract('lorem.txt', 'new_folder')
# Extract all files (no argument = extract on cwd)
example_zip.extractall('example')
example_zip.close()
