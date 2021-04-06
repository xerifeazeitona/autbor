import os
from PIL import Image, ImageDraw, ImageFont

# Drawing Shapes
img = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(img)
draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='black')
draw.rectangle((20, 30, 60, 60), fill='blue')
draw.ellipse((120, 30, 160, 60), fill='brown')
draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)), fill='red')
for i in range(100, 200, 10):
    draw.line([(i, 0), (200, i - 100)], fill='green')
img.save('drawing.png')

# Drawing Text
img = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(img)
draw.text((20, 150), 'Hello', fill='purple')
fonts_folder = '/usr/share/fonts/liberation-sans'
liberation_font = ImageFont.truetype(
    os.path.join(fonts_folder, 'LiberationSans-Regular.ttf'), 32)
draw.text((100, 150), 'Howdy', fill='gray', font=liberation_font)
img.save('text.png')
