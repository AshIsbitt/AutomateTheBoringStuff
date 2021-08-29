# upload/download and deleting spreadsheets

import ezsheets as ez

ss = ez.Spreadsheet('192MHvO4wOhpBf2-vMj3D4bv6Ocw7vH07J3RO7mhvZE8')

ss.downloadAsExcel('NewFilename.xlsx')
# Open Office
ss.downloadAsODS()

# These only download the first sheet
ss.downloadAsCSV()
ss.downloadAsTSV()

ss.downloadAsPDF()
ss.downloadAsHTML()

# Delete spreadsheet
ss2 = ez.Spreadsheet('1V5rpL5gTl39a7e5oFO95BXfh13iDjPihjEqpvawySiA')
ss2.delete()

# This will permanantly delete the file instead of sending it to trash
# ss2.delete(permanant=True)
