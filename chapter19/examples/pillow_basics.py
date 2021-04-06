from PIL import ImageColor
from PIL import Image

# Getting RGBA values with getcolor()
print(ImageColor.getcolor('red', 'RGBA'))
print(ImageColor.getcolor('RED', 'RGBA'))
print(ImageColor.getcolor('Black', 'RGBA'))
print(ImageColor.getcolor('chocolate', 'RGBA'))
print(ImageColor.getcolor('CornflowerBlue', 'RGBA'))

# Before proceding, check the coordinates and box tuples on the book

# Working with the image data type
cat_img = Image.open('zophie.png')
print(cat_img.size)
width, height = cat_img.size
print(width)
print(height)
print(cat_img.filename)
print(cat_img.format)
print(cat_img.format_description)
# Pillow automatically saves the image in the format provided in the extension
cat_img.save('zophie.jpg') 

# Creating images with Pillow
img = Image.new('RGBA', (100, 200), 'purple')
img.save('purple_image.png')
img2 = Image.new('RGBA', (20, 20))
img2.save('transparent_image.png') # (0, 0, 0, 0) is the default color

# Cropping images
cropped_img = cat_img.crop((335, 345, 565, 560))
cropped_img.save('cropped.png')

# Copying images
# Copying before pasting protects the original image because the paste
# is done in place (aka destructive)
cat_copy_img = cat_img.copy()

# Pasting images
# this method has 2 args: the image source, xy coord for where to paste
print(cropped_img.size)
cat_copy_img.paste(cropped_img, (0, 0))
cat_copy_img.paste(cropped_img, (400, 500))
cat_copy_img.save('pasted.png')

# Make a tiled img
cat_width, cat_height = cat_img.size
face_width, face_height = cropped_img.size
cat_copy_2 = cat_img.copy()
for left in range(0, cat_width, face_width):
    for top in range(0, cat_height, face_height):
        print(left, top)
        cat_copy_2.paste(cropped_img, (left, top))
cat_copy_2.save('tiled.png')

# Resizing an image
quarter_sized_img = cat_img.resize((int(width / 2), int(height / 2)))
quarter_sized_img.save('quartersized.png')
svelte_img = cat_img.resize((width, height + 300))
svelte_img.save('svelte.png')

# Rotating images
cat_img.rotate(90).save('rotated90.png')
cat_img.rotate(180).save('rotated180.png')
cat_img.rotate(270).save('rotated270.png')
# The rotate method has an optional expand argument to enlarge image
# dimensions to fit the entire rotated new image
cat_img.rotate(6).save('rotated6.png')
cat_img.rotate(6, expand=True).save('rotated6_expanded.png')

# Flipping images
cat_img.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
cat_img.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')

# Changing individual pixels
img = Image.new('RGBA', (100, 100))
print(img.getpixel((0, 0))) # getpixel returns RGBA value of said pixel
# paint top half light gray
for x in range(100):
    for y in range(50):
        img.putpixel((x, y), (210, 210, 210))
# paint bottom half dark gray
for x in range(100):
    for y in range(50, 100):
        img.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))
print(img.getpixel((0, 0)))
print(img.getpixel((0, 50)))
img.save('put_pixel.png')
