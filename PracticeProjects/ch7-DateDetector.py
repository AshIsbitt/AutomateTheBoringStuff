# Practice Project - date detection

import re
import sys
import pyperclip

def validateDateEntry(date):
	#empty variables for each section of the date
	day = 0
	month = 0
	year = 0
	leapyear = False

	#Break date into three variables and store them as integers
	day = int(date[0:2])
	month = int(date[3:5])
	year = int(date[6:10])

	#Check if year is between 1000 and 2999
	if (year < 1000) or (year > 2999):
		return False

	#Check if month is <= 12
	if month > 12:
		return False

	#Check leap year (year mod 4 is 0 unless year % 100 is also 0, then year % 400 must also be 0)
	if (year % 4 == 0) or (year % 100 == 0 and year % 400 == 0):
	 	leapyear == True

	#Check date < 31 (APR 4, JUN 6, SEP 9, NOV 11 < 30, FEB 2 < 28 unless leap year)
	if (day > 31) or (month == 4 and day > 30) or (
		month == 6 and day > 30) or (month == 9 and day > 30) or (
		month == 11 and day > 30) or (month == 2 and leapyear == True and day > 29) or (
		month == 2 and day > 28):

		return False

	#Otherwise, return the date
	return date


def regexChecker():
	#Empty list for correctly formatted dates returned
	datesList = []

	#Regex code
	dateRegex = re.compile(r'\d{2}/\d{2}/\d{4}')

	#If there's relevant text in the clipboard, check it for a date
	print("Checking clipboard")

	try:
		text = str(pyperclip.paste())
	except:
		#Otherwise, ask for entry from user
		print("Clipboard empty. Enter text:")
		text = input("")

	#Find the dates in the text
	for dates in dateRegex.findall(text):
		validatedDate = validateDateEntry(dates)

		#If they return, store them in a list. Otherwise, bin incorrect dates
		if validatedDate != False:
			datesList.append(validatedDate)
		else:
			continue


	for item in datesList:
		print(item)


print("DATE DETECTOR".center(10, "."))
regexChecker()


