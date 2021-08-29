# Creating Deleting sheets

import ezsheets as ez

ss = ez.createSpreadsheet('Multiple Sheets')
print(ss.sheetTitles)

ss.createSheet('Spam')
ss.createSheet('Eggs')
print(ss.sheetTitles)

# Create a sheet at index 0
ss.createSheet('Bacon', 0)
print(ss.sheetTitles)

# Empty sheet of all data
ss[0].clear()

# Delete sheet
ss[2].delete()
