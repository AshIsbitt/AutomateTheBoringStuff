# Change colour of individual pixel

from PIL import Image
from PIL import ImageColor

im = Image.new('RGBA', (100, 100))
print(im.getpixel((0, 0)))

for x in range(100):
    for y in range(50, 100):
        # getcolor accepts HTML color names, which you need to pass into putpixel, which does not
        im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))

print(im.getpixel((0, 0)))
print(im.getpixel((0, 50)))
