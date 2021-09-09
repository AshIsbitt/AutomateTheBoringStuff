# Create a new image with code

from PIL import Image

im = Image.new('RGBA', (100, 200), 'purple')
im.save('3-purpleImage.png')

im2 = Image.new('RGBA', (20, 20))
im2.save('3-transparentImage.png')
