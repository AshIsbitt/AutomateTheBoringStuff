# Get rows and columns from sheet 2

import openpyxl as xl
wb = xl.load_workbook('example.xlsx')
sheet = wb['Sheet1']

print(list(sheet.columns)[1])

for cellObj in list(sheet.columns)[1]:
	print(cellObj.value)
