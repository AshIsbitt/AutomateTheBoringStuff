# Optional Matching with the Question Mark

import re

batRegex = re.compile(r'Bat(wo)?man')
batRegexWithAsterisk = re.compile(r'Bat(wo)*man')
batRegexWithPlus = re.compile(r'Bat(wo)+man')

mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo3 = phoneRegex.search('my number is (415) 555-4242')
print(mo3.group())

mo4 = batRegexWithAsterisk.search('The Adventures of Batwowowowoman')
print(mo4.group())

mo5 = batRegexWithPlus.search('The Adventures of Batwoman')
print(mo5.group())