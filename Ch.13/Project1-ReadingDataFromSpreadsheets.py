# Reading Data from spreadsheets

'''
Spreadsheet cells:
A - tract number
B - state abbeviation
C - County name
D - tract pop
'''

import openpyxl
import pprint

print('Opening Workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData = {}

print('Reading rows...')
for row in range(2, sheet.max_row + 1):
	# Each row in spreadsheet has data for one tract
	state = sheet['B' + str(row)].value
	county = sheet['C' + str(row)].value
	pop = sheet['D' + str(row)].value

	# Check key for each state exists
	countyData.setdefault(state, {})
	# Check key for county in state exists
	countyData[state].setdefault(county, {'tracts':0, 'pop':0})

	# Each row represents one tract, so increment by one
	countyData[state][county]['tracts'] += 1
	# Increase county pop by pop in tract
	countyData[state][county]['pop'] += int(pop)

# Open new text file and write contents to it
print('Writing results...')
resultsFile = open('P1as_census2010.py', 'w')
resultsFile.write(f'allData = {pprint.pformat(countyData)}')
resultsFile.close()

print('Done.')






