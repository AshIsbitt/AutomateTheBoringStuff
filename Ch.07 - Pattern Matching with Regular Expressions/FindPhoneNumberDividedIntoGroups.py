# More Pattern Matching with Regular Expressions

import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
phoneNumRegexWithBrackets = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegexWithBrackets.search('my number is (415) 555-4242')

#This gets the parenthesis sections of the regex, with item 0 returning everything
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))

#get all the groups printed out with a visible division between them
print(mo.groups())

# In Regex, the following symbols all have special meaning:
# . ^ $ * + ? { } [ ] \ | ( )
# To use one, it needs to be "escaped" with a backslash before it 