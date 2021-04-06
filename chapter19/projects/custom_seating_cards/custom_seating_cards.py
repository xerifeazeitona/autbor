"""
Custom Seating Cards

Chapter 15 included a practice project to create custom invitations from
a list of guests in a word document. As an additional project, use the
pillow module to create images for custom seating cards for your guests.

For each of the guests listed in the guests.txt file, generate an image
file with the guest name and some flowery decoration. A public domain
flower image is also available.

To ensure that each seating card is the same size, add a black rectangle
on the edges of the invitation image so that when the image is printed
out, there will be a guideline for cutting.

The PNG files that Pillow produces are set to 72 pixels per inch, so a
4×5-inch card would require a 288×360-pixel image.
"""

import os
from PIL import Image, ImageDraw, ImageFont

FRAME_FILE = 'frame.png'
GUESTS_FILE = 'guests.txt'

def get_guest_list(filename):
    """Returns a justified list with all the names in 'filename'"""
    with open(filename) as file_obj:
        guests = file_obj.read().split('\n')
        return center_names(guests)

def center_names(names_list):
    """Returns a list with the names on 'names_list' center justified"""
    centered_names = []
    len_names = [len(name) for name in names_list]
    max_len = max(len_names)
    for name in names_list:
        centered_names.append(name.center(max_len))
    return centered_names

def draw_rectangle(image_obj):
    """Draws a black guideline for cutting the card."""
    draw = ImageDraw.Draw(image_obj)
    draw.rectangle((5, 5, 365, 293), outline='black')

def add_frame(image_obj):
    """Adds a flowery frame to the card."""
    frame = Image.open(FRAME_FILE)
    image_obj.paste(frame, (9, 9), frame)

def draw_guest_name(image_obj, guest_name):
    """Draws the guest name"""
    draw = ImageDraw.Draw(image_obj)
    font_folder = '/usr/share/fonts/urw-base35/'
    font_name = 'Z003-MediumItalic.otf' #afm otf t1
    font = ImageFont.truetype(
        os.path.join(font_folder, font_name), 54)
    draw.text((60, 130), guest_name, fill='black', font=font)

def create_card(guest_name):
    """Creates a seating card."""
    img = Image.new('RGBA', (370, 298), 'white')
    draw_rectangle(img)
    add_frame(img)
    draw_guest_name(img, guest_name)
    img.save(f'{guest_name.strip()}.png')

# Create guest list
guest_list = get_guest_list(GUESTS_FILE)
# Create a custom card for each guest in list
for guest in guest_list:
    create_card(guest)
