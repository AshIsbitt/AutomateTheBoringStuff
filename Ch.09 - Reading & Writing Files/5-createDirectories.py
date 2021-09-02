# Make directories

import os
from pathlib import Path

#This can create a whole subdirectory system
os.makedirs('../test/testing/created')

#This can only create one directory at a time and can't go deeper
Path(r'../moretesting').mkdir()