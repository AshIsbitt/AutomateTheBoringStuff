#Reading ZIP files

import zipfile as zf
import os
from pathlib import Path

p = Path('/Users/ashisbitt/Desktop/AutomateTheBoringStuff/Ch.10')
exampleZip = zf.ZipFile(p / 'some_folder.zip')

#This will return a list of the files and folders in the zipfile
print(exampleZip.namelist())

#This will get the info about a single file in the zip and get it's file size
spamInfo = exampleZip.getinfo('some_folder/spam.txt')
print(spamInfo.file_size)
print(spamInfo.compress_size)

print(f'Compressed file is {round(spamInfo.file_size / spamInfo.compress_size, 2)}x smaller!')
exampleZip.close()