# Spreadsheet attributes

import ezsheets as ez

ss = ez.Spreadsheet('192MHvO4wOhpBf2-vMj3D4bv6Ocw7vH07J3RO7mhvZE8')

print(ss.title)
ss.title = 'Class data'

print(ss.spreadsheetId)
print(ss.url)
print(ss.sheetTitles)
print(ss.sheets)
print(ss[0])
print(ss['Students'])
del ss[0]
print(ss.sheetTitles)

# If someone changes the spreadsheet online, you can update your
# object in the code with this
ss.refresh()
