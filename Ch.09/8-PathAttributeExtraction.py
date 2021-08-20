# Path attribute extraction

from pathlib import Path
import os

p = Path('/Desktop/AutomateTheBoringStuff/Ch.9/1-multiplatformPaths.py')

print(p.anchor)
print(p.parent)
print(p.name)
print(p.stem)
print(p.suffix)

#Unlike "parent", "parents" is a list that follows the whole path
# This will crash if the index is too high
print(p.parents[0])
print(p.parents[3])

# Getting Dir and Base name

print(os.path.basename(p))
print(os.path.dirname(p))

#This returns a tuple version of the directory and the filename
print(os.path.split(p))

#Return a list of all items in the path by using the string split function on the path separator
print(str(p).split(os.sep))