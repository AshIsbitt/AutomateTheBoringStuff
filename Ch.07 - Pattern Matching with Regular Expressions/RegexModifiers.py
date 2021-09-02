# Caret and Dollar Sign Characters

import re

# Caret symbol ^ is used at the start of a regex to indicate only to check at the start
beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search('Hello World'))

# Dollar symbol $ is used at the end of a regex to indicate only to check at the end
endsWithNumber = re.compile(r'\d$')
print(endsWithNumber.search('Your number is 42'))

#If both are used, it must encompass the entire string
wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('1234567890'))