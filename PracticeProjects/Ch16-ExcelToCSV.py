# Excel-to-CSV Converter

import openpyxl
import csv
import os
from pathlib import Path

# Skip non-excel files
for excelFile in os.listdir('./excelSpreadsheets/'):
    print(f'Opening {excelFile}...')

    wb = openpyxl.load_workbook(os.path.join('excelSpreadsheets', excelFile))

    # Loop through all sheets in workbook
    for sheetName in wb.get_sheet_names():
        sheet = wb.get_sheet_by_name(sheetName)

        # Create CSV filename from excel filename and sheet name
        filename = f"{str(excelFile[:-5])}-{str(sheet.title)}"

        # Create CSV writer
        Path.mkdir('./excelSpreadsheets/outputCSVfiles', exist_ok=True)
        csvFile = open(os.path.join('excelSpreadsheets', 'outputCSVfiles'), 'w')

    #     # Loop through every row in the sheet
    #     for rowNum in range(1, sheet.max_row + 1):
    #         rowData = []

    #         for colNum in range(1, sheet.max_column + 1):
    #             # Append each cell to rowData

    #             # write rowData list to CSV file

    # csvFile.close()
