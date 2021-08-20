#Moving files

import shutil
from pathlib import Path

p = Path('/Users/ashisbitt/Desktop/AutomateTheBoringStuff/Ch.10')

#This will move the eggs.txt file into the Eggs folder on the desktop, as long as it already exists
#It will also rename the file to new_Eggs.txt
print(shutil.move(p / 'eggs.txt', p / '../../Eggs/new_eggs.txt'))