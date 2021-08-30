# Project - Find mistake in spreadsheet
# Note - to run this locally, you need to make sure this file is in the same directory as the credentials and
# Pickle files from Ch.14

import ezsheets

# Spreadsheet provided by book
ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
ss2 = ezsheets.createSpreadsheet('UpdatedBeanCounter')

# Get sheet
sheet = ss[0]

# Create headings on SS2
newSheet = ss2[0]
newSheet['A1'] = 'BEANS PER JAR'
newSheet['B1'] = 'JARS'
newSheet['C1'] = 'TOTAL BEANS'

print("Calculating...")

# Loop through each item
for item in range(2, sheet.rowCount):
    print(item)

    # Multiply the A and B columns if they aren't empty
    if sheet[f'A{item}'] != '':
        newVal = int(sheet[f'A{item}']) * int(sheet[f'B{item}'])

    # Add new maths result to ss2
    newSheet[f'A{item}'] = sheet[f'A{item}']
    newSheet[f'B{item}'] = sheet[f'B{item}']
    newSheet[f'C{item}'] = newVal

print("Done!")
