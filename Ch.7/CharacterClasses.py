# Character Classes

import re

# \d - Any numeric digit
# \D - Any character that's not a numeric digit
# \w - Any letter, number, or underscore
# \W - Any character that's not a letter, number or underscore
# \s - Any space, tab or newline
# \S - Any character that's not a space, tab, or newline

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 Drummers, 11 Pipers, 10 Lord, 9 Ladies, 8 Maids, 7 Swans, 6 Geese, 5 Rings, 4 Birds, 3 Hens, 2 Doves, 1 Partridge'))

# Making your own using square brackets
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats baby food. BABY FOOD!'))

#Inverting using a ^ Caret key
vowelRegex = re.compile(r'[^aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats baby food. BABY FOOD!'))