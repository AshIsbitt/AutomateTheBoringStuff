# Walking through directories

import os
from pathlib import Path

p = Path('/Users/ashisbitt/Desktop/AutomateTheBoringStuff/Ch.10')

for folderName, subfolders, filenames in os.walk(p / 'some_folder'):
	print("The current folder is: " + folderName)

	for subFolder in subfolders:
		print("SUBFOLDER OF " + folderName + ": " + subFolder)

	for filename in filenames:
		print("FILE INSIDE " + folderName + ":" + filename)

	print('')