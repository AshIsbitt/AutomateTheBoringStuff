# Freezing panes

import openpyxl as xl

wb = xl.load_workbook('produceSales.xlsx')
sheet = wb.active

sheet.freeze_panes = 'A2'

wb.save('freezePanes.xlsx')
