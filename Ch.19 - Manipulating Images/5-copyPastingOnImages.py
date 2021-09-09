# Copying and pasting images

from PIL import Image

catIm = Image.open('zophie.png')
copyCatIm = catIm.copy()

faceIm = catIm.crop((335, 345, 565, 560))
copyCatIm.paste(faceIm, (0,0))
copyCatIm.paste(faceIm, (400, 500))

copyCatIm.save('5-Pasted.png')

catIm_width, catIm_height = catIm.size
faceIm_width, faceIm_height = faceIm.size

catCopy2 = catIm.copy()
for left in range(0, catIm_width, faceIm_width):
    for top in range(0, catIm_height, faceIm_height):
        print(left, top)
        catCopy2.paste(faceIm, (left, top))

catCopy2.save('5-catTiled.png')
