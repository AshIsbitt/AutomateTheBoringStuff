# Mad Libs project

'''
Usage:
python3 madlibs.py <file> - Runs the madlibs program through a .txt file
'''

import sys
from pathlib import Path
import pyinputplus as pyin
import re

userFile = ""

#Check if file is .txt and Open file
if len(sys.argv) == 2 and sys.argv[1][-4:] == '.txt':
	userFile = open(str(sys.argv[1]), 'r')
	madLibContent = userFile.read()
else:
	print("file not found")

# Read through the file and find words in all caps

textRegex = re.compile(r"(ADJECTIVE|NOUN|VERB|ADVERB)")

madLibList = madLibContent.split(" ")

for item in range(len(madLibList)):
	#Detect what type of word it's asking for
 	#Ask user to fill that slot	
	if textRegex.search(madLibList[item]) != None:
		userReplace = input("Enter a(n) %s: " % madLibList[item].lower())

		if madLibList[item][-1] == ".":
			madLibList[item] = userReplace + "."
		else:
			madLibList[item] = userReplace

#Print final madlib to the console
madLibFinalStr = ' '.join(madLibList)
print(madLibFinalStr)
