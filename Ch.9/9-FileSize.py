# File sizes and folder contents

from pathlib import Path
import os

p = Path('/Users/ashisbitt/Desktop/AutomateTheBoringStuff/Ch.9/1-multiplatformPaths.py')
print(os.path.getsize(p))

p2 = Path('/Users/ashisbitt/Desktop/AutomateTheBoringStuff/Ch.9')
print(os.listdir(p2))

#get total size of files in directory
totalSize = 0

for filename in os.listdir(p2):
	totalSize = totalSize + os.path.getsize(os.path.join(p2, filename))

print(totalSize)