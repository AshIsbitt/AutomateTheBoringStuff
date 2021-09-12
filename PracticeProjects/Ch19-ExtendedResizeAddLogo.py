# Adding a logo

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.SQUARE_FIT_SIZE

os.makedirs('withLogo', exist_ok=True)

# Loop over all files in the working directory
for filename in os.listdir('.'):

    # Skip non-image files and the logo image
    # EXTENDED: to handle GIF and BMP files
    # EXTENDED: to handle all cases of given formats (IE JPG and jpg)
    if not (filename.endswith('.png'.lower()) or filename.endswith('.jpg'.lower()) or filename.endswith('.GIF'.lower()) or filename.endswith('.BMP'.lower())) or filename == LOGO_FILENAME:
        continue

    im = Image.open(filename)
    width, height = im.size

    # EXTENDED: skip if the image is less than double the size of the logo
    if (width < (logoWidth * 2)) or (height < (logoHeight * 2)):
        continue

    # Check if image needs to be resized
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        # Resize the image
        print(f'Resizing {filename}...')
        im - im.resize(width, height)

    # Add the logo
    print(f'Adding logo to {filename}...')
    # The third argument here (the seccond 'logoIm') makes sure the background of the logo is transparent
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

    # Save changes
    im.save(os.path.join('withLogo', filename))
