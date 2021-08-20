# Substituting strings

import re

#This replaces the "Agent" and the next word after, with the word "CENSORED"
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

#This version allows for the first letter of each Agent's name to be revealed and the rest to be asterisked out
namesRegex2 = re.compile(r'Agent (\w)\w*')
print(namesRegex2.sub(r'\1****', 'Agent Alice gave the secret documents to Agent Bob.'))