#Detect date from input
print("Enter Date:")
dateEntry = input("")

dateRegex = re.compile(r'\d{2}/\d{2}/\d{4}')
dateChecked = dateRegex.search(dateEntry)

#store in Day Month Year variables
day = 0
month = 0
year = 0

if dateChecked != None:
	day = dateEntry[0:2]
	month = dateEntry[3:5]
	year = dateEntry[6:10]
else:
	print("Please try again")
	sys.exit()

#validate each variable
if int(year) < 1000 or int(year) > 2999:
	print("Error: incorrect year")	
elif int(month) > 12:
	print("Error: incorrect month")
elif not (int(year) % 100 == 1 and int(year) % 4 == 1 and int(month) == 2 and int(day) == 29):
	print("Error: leap year detected")
elif int(day) > 31 or (int(month) == 2 and int(day) > 28) or (int(month) == 4 and int(day) > 30) or (int(month) == 6 and int(day) > 30) or (int(month) == 9 and int(day) > 30) or (int(month) == 11 and int(day) > 30):
	print("Error: incorrect day")

#validate leap years
