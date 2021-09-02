# excel formulas

import openpyxl as xl
wb = xl.Workbook()
sheet = wb.active

sheet['A1'] = 200
sheet['A2'] = 300
sheet['A3'] = '=SUM(A1:A2)'

wb.save('writeFormula.xlsx')