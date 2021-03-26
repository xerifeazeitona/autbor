"""
Filling in the Gaps

Write a program that ﬁnds all ﬁles with a given preﬁx, such as
*spam001.txt*, *spam002.txt*, and so on, in a single folder and locates
any gaps in the numbering (such as if there is a *spam001.txt* and
*spam003.txt* but no *spam002.txt* ).
Have the program rename all the later ﬁles to close this gap.
"""

import os
import re
import shutil

regex = re.compile(r'(^\w*)(\d\d\d)(.*$)')
target_folder = os.getcwd() + '/sample_data'

files = os.listdir(target_folder)   # all files in the folder
valid_files = []                    # only the files that match the pattern
actual_sequence = []                # numbers extracted from the list of files

# Walk through the list of files
for filename in files:
    mo = regex.search(filename)
    # Skip files without a sequence
    if not mo:
        continue
    # extract the numeric part from the filename
    sequence_part = int(mo.group(2))
    actual_sequence.append(sequence_part)
    valid_files.append(filename)

# Create a list of numbers that aren't on the actual sequence
proper_sequence = list(range(1, len(files) + 1)) 
missing_numbers = []
for number in proper_sequence:
    if number not in actual_sequence:
        missing_numbers.append(number)

# Get the different parts of the filename
mo = regex.search(valid_files[0])
before_part = mo.group(1)
after_part = mo.group(3)

# Create a list with the proper filename for missing numbers
new_files = []
for number in missing_numbers:
    if number < 10:
        new_files.append(f'{before_part}00{number}{after_part}')
    elif number < 100:
        new_files.append(f'{before_part}0{number}{after_part}')
    else:
        new_files.append(f'{before_part}{number}{after_part}')

# Create a list of files to be renamed
valid_files.sort()
old_files = valid_files[-1*len(missing_numbers):]

# Actually rename the files
for filename in old_files:
    old_file = os.path.join(target_folder, filename)
    new_file = os.path.join(target_folder, new_files[old_files.index(filename)])
    print(f'renaming {os.path.basename(old_file)} to {os.path.basename(new_file)}')
    #shutil.move(old_file, new_file) # uncomment to run for real
