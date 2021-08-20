#Copy entire directories

import shutil
import os 
from pathlib import Path

p = Path('/Users/ashisbitt/Desktop/')

#This should copy Ch.10 folder and all of it's contents onto the desktop into a new folder 
shutil.copytree(p/'AutomateTheBoringStuff/Ch.10', p/'ch10-copy')