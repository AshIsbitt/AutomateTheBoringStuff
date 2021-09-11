# Rotate image

from PIL import Image

catIm = Image.open('zophie.png')

# If this isn't an exact square, (IE rotating by 45 degrees), the rest is filled in with transparent pixels on mac
catIm.rotate(90).save('6-rotated90.png')
catIm.rotate(180).save('6-rotated180.png')
catIm.rotate(270).save('6-rotated270.png')

catIm.transpose(Image.FLIP_LEFT_RIGHT).save('6-horizontal_flip.png')
catIm.transpose(Image.FLIP_TOP_BOTTOM).save('6-vertical_flip.png')
