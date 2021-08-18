# Absolute and Relative paths

from pathlib import Path

#True
print(Path.cwd().is_absolute())

#False
print(Path('../Ch.7/Findall.py').is_absolute())

print(Path.cwd() / Path('../Ch.7/Findall.py'))

print(Path.home() / Path('/Desktop/AutomateTheBoringStuff/Ch.7'))