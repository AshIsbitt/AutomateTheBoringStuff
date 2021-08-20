#Using Regex

import pyinputplus as pyin

#This tells the inputNum to use regex statements as well for roman numeral input
response = pyin.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
print(response)

#blockRegexes instead will blacklist a regex expression from being allowed as input
response2 = pyin.inputNum(blockRegexes=[r'[02468]$'])
print(response2)

#Note: allowRegexes takes precedence over blockRegexes
response3 = pyin.inputStr(allowRegexes=[r'caterpillar', 'category'], blockRegexes=[r'cat'])
print(response3)