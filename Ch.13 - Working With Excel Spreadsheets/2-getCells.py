# Getting cells from a sheet

import openpyxl as xl

wb = xl.load_workbook('example.xlsx')
sheet = wb['Sheet1']

# Get cell from sheet
print(sheet['A1'])
print(sheet['A1'].value)

# Get row, column, value
c = sheet['B1']
print(c.value)
print(f'Row: {c.row}, Column:{c.column} is {c.value}')
print(f'Cell {c.coordinate} is {c.value}')
