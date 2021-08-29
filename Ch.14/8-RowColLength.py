# Length of Rows and Cols

import ezsheets as ez

ss = ez.Spreadsheet('produceSales')
sheet = ss[0]

print(sheet.rowCount)
print(sheet.columnCount)

sheet.columnCount = 4
print(sheet.columnCount)
