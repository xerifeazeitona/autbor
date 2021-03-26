"""
The shutil (or shell utilities) module has functions to let you copy,
move, rename, and delete ﬁles in your Python programs.
"""
import shutil
import os
from pathlib import Path

p = Path.home() / 'Documents'
Path(p / 'some_folder').mkdir()

# Calling shutil.copy(source, destination) will copy the ﬁle at the path
# source to the folder at the path destination.
shutil.copy(p / 'test.py', p / 'some_folder')
# You can change the filename in the destination
shutil.copy(p / 'test.py', p / 'some_folder/test2.py')

# While shutil.copy() will copy a single ﬁle, shutil.copytree() will
# copy an entire folder and every folder and ﬁle contained in it.
shutil.copytree(p / 'some_folder', p / 'some_folder_backup')

# Calling shutil.move(source, destination) will move the ﬁle or folder
# at the path source to the path destination
shutil.move(p / 'some_folder/test.py', p / 'some_folder_backup/test3.py')

# Calling os.unlink.(path) will delete the file at path
os.unlink(p / 'some_folder/test2.py')
# Calling os.rmdir(path) will delete the folder at path (folder must be empty)
os.rmdir(p / 'some_folder')
# Calling shutil.rmtree(path) will remove the folder at path,
# and all files and folders it contains
shutil.rmtree(p / 'some_folder_backup')
