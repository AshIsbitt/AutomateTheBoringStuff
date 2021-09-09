# Opening images

from PIL import Image

catImage = Image.open('zophie.png')
print(catImage)

print(catImage.size)

width, height = catImage.size
print(width)
print(height)

print(catImage.filename)
print(catImage.format)
print(catImage.format_description)

# Save image with changes
catImage.save('zophie.zpg')
