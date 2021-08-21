#Extracting ZIPs

import zipfile as zf
import os
from pathlib import Path

p = Path('/Users/ashisbitt/Desktop/AutomateTheBoringStuff/Ch.10')
p2 = Path('/Users/ashisbitt/Desktop')
exampleZip = zf.ZipFile(p / 'some_folder.zip')

#By default, this will extract to CWD
exampleZip.extractall(p2/'extracted_folder')

#This will only extract a single file from the ZIP. The second arguement will tell it where to extract to
exampleZip.extract('some_folder/spam.txt', p2)

exampleZip.close()