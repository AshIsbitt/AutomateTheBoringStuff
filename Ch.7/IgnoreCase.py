# Case insensetive matching

import re 

# You can ignore the case you're looking at by using re.IGNORECASE, or re.I

robocop = re.compile(r'robocop', re.IGNORECASE)
print(robocop.search('RoboCop is part man, part machine').group())