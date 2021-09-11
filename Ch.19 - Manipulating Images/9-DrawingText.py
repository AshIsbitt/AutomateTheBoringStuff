# Drawing text

from PIL import Image, ImageDraw, ImageFont
import os

im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)
draw.text((20, 150), 'Hello', fill='purple')

fontsFolder = '/Library/Fonts'
arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'Ubuntu-R.ttf'), 32)
draw.text((100, 150), 'Howdy', fill='gray', font=arialFont)

im.save('9-text.png')
