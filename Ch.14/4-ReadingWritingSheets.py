# reading/writing data 

import ezsheets as ez

ss = ez.createSpreadsheet('YetAnotherSpreadsheet')

sheet = ss[0]
print(sheet.title)

sheet['A1'] = 'Name'
sheet['B1'] = 'Age'
sheet['C1'] = 'Favourite Movie'

print(sheet['A1'])

# This also gets cell B1
print(sheet[2,1])

sheet['A2'] = 'Alice'
sheet['B2'] = 30
sheet['C2'] = 'Robocop'
