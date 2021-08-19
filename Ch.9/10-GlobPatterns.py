# Glob Patterns

#These are like command line based regex that lists the contents of a folder

from pathlib import Path

p = Path('/Users/ashisbitt/Desktop/AutomateTheBoringStuff/')

#This returns an object.
#print(p.glob('*'))

#print(list(p.glob('*')))

#This will return all the items in the path with the .md extention
#print(list(p.glob('*.md')))

#An asterisk stands for any single character - this won't return "Ch.10"
print(list(p.glob('Ch.?')))

for i in p.glob('Ch.7/*.py'):
	print(i)