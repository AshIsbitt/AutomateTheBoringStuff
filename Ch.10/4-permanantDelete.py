# Deleting files and folders

import shutil
import os
from pathlib import Path
import send2trash

'''This will permanantly delete files. It's better practice to run this code a few times with
the delete code commented out and instead print out the names of the files to be deleted until
you are sure there aren't any issues in the code
'''

# p = Path('/Users/ashisbitt/Desktop/AutomateTheBoringStuff/Ch.10')

# os.unlink(p / 'spam.txt')

'''Instead, a safer way to delete files is the third party send2Trash module, which needs to 
be installed in pip first.
'''

#Create a file to delete
baconFile = open('bacon.txt', 'a')
baconFile.write("Bacon is not a vegetable")
baconFile.close()


send2trash.send2trash('bacon.txt')