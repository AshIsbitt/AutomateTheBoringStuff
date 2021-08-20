# Path validity

from pathlib import Path

p1 = Path("/Users/ashisbitt/Desktop/")
p2 = Path("/Users/ashisbitt/Desktop/fakeFolder")
p3 = Path('/Users/ashisbitt/Desktop/AutomateTheBoringStuff/Ch.9/1-multiplatformPaths.py')

#True
print(p1.is_dir())
#False - you can use this method to see if an external drive is present
print(p2.exists())
#True
print(p3.is_file())