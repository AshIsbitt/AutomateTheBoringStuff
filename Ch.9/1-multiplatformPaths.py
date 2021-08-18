#multi-platform file paths

from pathlib import Path

location = Path('spam', 'bacon', 'eggs')
print(location)

#When using windows, this will print out a path with escaped backslashes
print(str(location))