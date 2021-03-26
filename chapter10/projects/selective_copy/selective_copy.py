"""
Selective Copy

Write a program that walks through a folder tree and searches for ﬁles
with a certain ﬁle extension (such as .pdf or .jpg).
Copy these ﬁles from whatever location they are in to a new folder.
"""

import os
import shutil

def selective_copy(source, destination, extension):
    """Copies files with the provided extension from source to destination"""
    if not os.path.exists(destination):
        os.mkdir(destination)

    for folder, _, files in os.walk(source):
        print(f'\nChecking {os.path.basename(folder)}...')
        for filename in files:
            if filename.endswith(extension):
                print(f'{filename} copied to {os.path.basename(destination)}')
                shutil.copy(
                    os.path.join(folder, filename),
                    os.path.join(destination, filename))
    print('\n...done!')

source_folder = os.getcwd() + '/sample_data'
destination_folder = os.getcwd() + '/new_folder'
target_extension = 'pdf'
selective_copy(source_folder, destination_folder, target_extension)
