# Joining Paths

from pathlib import Path

#This is better than using the + concatenation as this won't matter about the OS you're on
print(Path('spam') / 'bacon' / 'eggs')

print(Path('spam') / Path('bacon/eggs'))

print(Path('spam') / Path('bacon', 'eggs'))