# Finding Patterns of Text with Regular Expressions

#import regex module
import re

#What to search for
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

#String to search though
mo = phoneNumRegex.search('my number is 415-555-4242')

#Result comes as an object with a .group() method
print('phone number found: ' + mo.group())