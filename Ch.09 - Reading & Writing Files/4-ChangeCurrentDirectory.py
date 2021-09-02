# Current working directory

from pathlib import Path
import os

print(Path.cwd())
os.chdir('/Users/ashisbitt/Desktop/AutomateTheBoringStuff/Ch.8')
print(Path.cwd())

#This is an older version of the Path.cwd method and isn't worth using. 
print(os.getcwd())