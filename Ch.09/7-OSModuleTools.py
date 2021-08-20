# OS module tools

import os
from pathlib import Path

#Return a string of the absolute path
print(os.path.abspath(Path.cwd()))

#return True if the arguement is absolute
print(os.path.isabs(Path.cwd()))

# Will return a relative path from arg2 to arg1 locations
print(os.path.relpath(Path.cwd(), '../Ch.7'))