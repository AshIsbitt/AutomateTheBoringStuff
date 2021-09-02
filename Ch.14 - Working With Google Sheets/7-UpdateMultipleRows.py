# Get all rows

import ezsheets as ez

ss = ez.Spreadsheet('produceSales')
sheet = ss[0]

rows = sheet.getRows()
print(rows[0])

rows[1][0] = 'PUMPKIN'
print(rows[1])

print(rows[10])
rows[10][2] = '400'
rows[10][4] = '904'
print(rows[10])

sheet.updateRows(rows)
