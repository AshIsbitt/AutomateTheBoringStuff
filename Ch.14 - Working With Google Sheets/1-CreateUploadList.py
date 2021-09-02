# Creating, uploading, listing spreadsheets

import ezsheets

# Get spreadsheet by it's URL ID
# If only one spreadsheet of that name exists, you can also
# pass the spreadsheet title
ss = ezsheets.Spreadsheet('192MHvO4wOhpBf2-vMj3D4bv6Ocw7vH07J3RO7mhvZE8')
print(ss)

print(ss.title)

# Create spreadsheet
# ss2 = ezsheets.createSpreadsheet('New Spreadsheet')
# print(ss2.title)

# Uploading spreadsheet
# ss3 = ezsheets.upload('../Ch.13/censuspopdata.xlsx')
# print(ss3.title)

# List spreadsheets
print(ezsheets.listSpreadsheets())
