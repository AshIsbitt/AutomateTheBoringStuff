# Get rows and columns from sheet

import openpyxl as xl
wb = xl.load_workbook('example.xlsx')
sheet = wb['Sheet1']

allCells = tuple(sheet['A1':'C3'])

for rowOfCellObjects in sheet['A1':'C3']:
	for cellObj in rowOfCellObjects:
		print(cellObj.coordinate, cellObj.value)
	print('---End of Row---')
