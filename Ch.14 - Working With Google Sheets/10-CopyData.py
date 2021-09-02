# Copying sheets

import ezsheets as ez

ss1 = ez.createSpreadsheet('First Spreadsheet')
ss2 = ez.createSpreadsheet('Second Spreadsheet')

print(ss1[0])
ss1[0].updateRow(1, ['Some', 'Data', 'In', 'The', 'First', 'Row'])

# Copy the first sheet from spreadsheet1 to spreadsheet2
ss1[0].copyTo(ss2)
ss2.sheetTitles
