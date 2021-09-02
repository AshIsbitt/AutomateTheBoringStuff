# Entire Rows and Columns

import ezsheets as ez

ss = ez.upload('../Ch.13/produceSales.xlsx')
sheet = ss[0]

print(sheet.getRow(1))
print(sheet.getRow(2))

colOne = sheet.getColumn(1)
print(colOne)

print(sheet.getRow(3))
sheet.updateRow(3, ['Pumpkin', '11.50', '20', '230'])
print(sheet.getRow(3))

for i, value in enumerate(colOne):
    colOne[i] = value.upper()

sheet.updateColumn(1, colOne)
