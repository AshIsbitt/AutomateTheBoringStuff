# Writing values to cells

import openpyxl as xl

wb = xl.Workbook()
sheet = wb['Sheet']

sheet['A1'] = 'Hello world'
print(sheet['A1'].value)
