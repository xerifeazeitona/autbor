#! /usr/bin/env python3
"""
backup_to_zip - Copies an entire folder and its contents into a ZIP file
whose filename increments.
"""

import os
import zipfile

def backup_to_zip(folder):
    """Back up the entire contents of "folder" into a ZIP file."""
    folder = os.path.abspath(folder) # Make sure the folder is absolute

    # Figure out the filename this code should use based on what files
    # already exist.
    number = 1
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_filename):
            break
        number += 1

    # Create the ZIP file
    print(f'Creating {zip_filename}...')
    backup_zip = zipfile.ZipFile(zip_filename, 'w')

    # Walk the entire folder tree and compress the files in each folder
    for foldername, _, filenames in os.walk(folder):
        print(f'Adding files in ./{os.path.basename(folder)}' \
            f'/{os.path.basename(foldername)}...')

        # Add all the files in this folder to the ZIP file
        for filename in filenames:
            new_base = os.path.basename(folder) + '_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue # don't backup the backup ZIP files
            abs_name = os.path.join(foldername, filename)
            arc_name = abs_name[len(folder) + 1:]
            backup_zip.write(abs_name, arcname=arc_name)
    backup_zip.close()

    print('...done!')

backup_to_zip(f'{os.getcwd()}/spam')
