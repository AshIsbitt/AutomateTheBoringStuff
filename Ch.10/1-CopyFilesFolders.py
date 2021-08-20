# copying files and folders

import shutil
import os 
from pathlib import Path

p = Path('/Users/ashisbitt/Desktop/AutomateTheBoringStuff/Ch.10')

#The copy function won't delete the old files

#Note that this will only work if some_folder already exists
print(shutil.copy(p / 'spam.txt', p / 'some_folder'))

#This will copy the contents of "eggs.txt" to the new file "eggs2.txt"
print(shutil.copy(p/'eggs.txt', p/'some_folder/eggs2.txt'))