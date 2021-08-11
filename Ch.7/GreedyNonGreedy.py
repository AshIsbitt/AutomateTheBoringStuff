# Greedy and Non Greedy Matching

import re

# Regex is greedy by default meaning it'll find the longest possible result

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

#This use of the ? in the below regex is unrelated to it's use to flag an optional group

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())