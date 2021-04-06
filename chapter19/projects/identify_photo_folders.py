#! /usr/bin/env python3
"""
Identifying Photo Folders on the Hard Drive

Write a program that goes through every folder on your hard drive and
finds potential photo folders. Of course, first you’ll have to define
what you consider a “photo folder” to be; let’s say that it’s any folder
where more than half of the files are photos. And how do you define what
files are photos?
First, a photo file must have the file extension .png or .jpg. Also,
photos are large images; a photo file’s width and height must both be
larger than 500 pixels. This is a safe bet, since most digital camera
photos are several thousand pixels in width and height.
"""

import os
from PIL import Image

def is_image_file(file_name):
    """Returns True if 'filename' is a image file."""
    valid_extensions = ['.jpg', '.png']
    for extension in valid_extensions:
        if file_name.lower().endswith(extension):
            return True
    return False


for folder, subfolder, files in os.walk('/'):
    num_photo_files = 0
    num_non_photo_files = 0
    for filename in files:
        # Check if file is a photo
        if not is_image_file(filename):
            num_non_photo_files += 1
            continue

        # Open image file
        try:
            img = Image.open(os.path.join(os.path.abspath(folder), filename))
        except:
            continue

        # Check if width and height are larger than 500
        width, height = img.size
        if width > 500 and height > 500:
            num_photo_files += 1
        else:
            num_non_photo_files += 1

    if num_photo_files > ((num_photo_files + num_non_photo_files) / 2):
        print(os.path.abspath(folder))
