#Project 2 - Writing excel documents

import openpyxl as xl

# Creating empty workbook
wb = xl.Workbook()

print(wb.sheetnames)
sheet = wb.active
print(sheet.title)

# Set worksheet title
sheet.title = 'Spam bacon eggs Sheet'

# Changes to a spreadsheet wont be saved until you save it
wb.save('example_2.xlsx')