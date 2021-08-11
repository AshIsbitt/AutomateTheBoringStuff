# Wildcard Character

import re

# The dot . character will match any symbol apart from a newline
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

#Matching everything
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))

# Note that the . is a greedy modifier. To match all text in a non-greedy way, include a ?
nongreedyRegex = re.compile(r'<.*?>')
mo2 = nongreedyRegex.search('<To serve man> for dinner>')
print(mo2.group())

greedyRegex = re.compile(r'<.*>')
mo3 = greedyRegex.search('<To serve man> for dinner>')
print(mo3.group())

#re.DOTALL makes the . match a newline too
noNewLineRegex = re.compile(r'.*')
mo4 = noNewLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print(mo4)

newLineRegex = re.compile(r'.*', re.DOTALL)
mo5 = newLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print(mo5)