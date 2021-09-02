#Changing date styles in files names

import shutil
import os
import re

#Create a regex that matches files with the american date format
datePattern = re.compile(r"""^(.*?)			#All text before date
	((0|1)?\d)-								#month
	((0|1|2|3)?\d)-							#Day
	((19|20)\d\d)							#Year
	(.*?)$									#All text after date
	""", re.VERBOSE)

#Loop over files in working directory
for amerFilename in os.listdir('.'):
	mo = datePattern.search(amerFilename)

	#skip files without a date
	if mo == None:
		continue

	#Get the different parts of the filename
	beforePart = mo.group(1)
	monthPart = mo.group(2)
	dayPart = mo.group(4)
	yearPart = mo.group(6)
	afterPart = mo.group(8)

	#Form the european-style filename
	euroFileName = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

	#Get the full absolute path
	absWorkingDir = os.path.abspath('.')
	amerFilename = os.path.join(absWorkingDir, amerFilename)
	euroFileName = os.path.join(absWorkingDir, euroFileName)

	#Rename file
	print(f'Renaming "{amerFilename}" to "{euroFileName}"...')
	shutil.move(amerFilename, euroFileName)
