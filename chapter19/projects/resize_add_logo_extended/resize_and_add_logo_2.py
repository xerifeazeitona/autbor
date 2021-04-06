#! /usr/bin/env/python3
"""
Extending and Fixing the Chapter Project Programs

The resizeAndAddLogo.py program in this chapter works with PNG and JPEG
files, but Pillow supports many more formats than just these two.
Extend resizeAndAddLogo.py to process GIF and BMP images as well.

Another small issue is that the program modifies PNG and JPEG files only
if their file extensions are set in lowercase. For example, it will
process *zophie.png* but not *zophie.PNG*. Change the code so that the
file extension check is case insensitive.

Finally, the logo added to the bottom-right corner is meant to be just a
small mark, but if the image is about the same size as the logo itself,
the result will look weird.
Modify resizeAndAddLogo.py so that the image must be at least twice the
width and height of the logo image before the logo is pasted. Otherwise,
it should skip adding the logo.
"""

import os
from PIL import Image

def is_image_file(file_name):
    """Returns True if 'filename' is a image file."""
    valid_extensions = ['.jpg', '.png', '.gif', '.bmp']
    for extension in valid_extensions:
        if file_name.lower().endswith(extension):
            return True
    return False

# using constants makes your code easier to maintain
SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logo_img = Image.open(LOGO_FILENAME)
logo_img = logo_img.resize((75, 75)) # needed resize cause logo is huge
logo_width, logo_height = logo_img.size

os.makedirs('with_logo', exist_ok=True)
# Loop over all files in the working directory
for filename in os.listdir():
    if not is_image_file(filename) or filename == LOGO_FILENAME:
        continue # skip non-imag files and the logo file itself
    img = Image.open(filename)
    width, height = img.size

    # Check if the image is big enough to fit the logo
    if width < (logo_width * 2) or height < (logo_height * 2):
        continue

    # Check if image needs to be resized
    if width > SQUARE_FIT_SIZE or height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
        # Resize the image
        print(f'Resizing {filename}...')
        img = img.resize((width, height))

    # Add the logo
    print(f'Adding logo to {filename}')
    img.paste(logo_img, (width - logo_width, height - logo_height), logo_img)

    # Save changes
    img.save(os.path.join('with_logo', filename))
