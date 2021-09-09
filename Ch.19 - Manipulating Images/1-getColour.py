# Get a specific colour

from PIL import ImageColor

# This function takes any colour recognised by HTML

# These are the same
print(ImageColor.getcolor('red', 'RGBA'))
print(ImageColor.getcolor('RED', 'RGBA'))

print(ImageColor.getcolor('black', 'RGBA'))
print(ImageColor.getcolor('Chocolate', 'RGBA'))
print(ImageColor.getcolor('CornflowerBlue', 'RGBA'))
