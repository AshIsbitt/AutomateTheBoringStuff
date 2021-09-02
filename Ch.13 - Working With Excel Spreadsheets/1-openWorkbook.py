# open workbook

import openpyxl as xl

wb = xl.load_workbook('example.xlsx')
print(type(wb))

# Get workbooks
print(wb.sheetnames)

# Get a sheet from the workbooks
sheet = wb['Sheet3']
print(sheet)
print(type(sheet))
print(sheet.title)

# Get active sheet
activeSheet = wb.active
print(activeSheet)