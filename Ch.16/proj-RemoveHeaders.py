# Project - Remove Header from CSV

import csv
import os

os.makedirs('headerRemoved', exist_ok=True)

# Loop through each CSV file
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue

    print(f'Removing header from: {csvFilename}...')

    # Read the CSV file in, skipping first row
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)

    # Loop through each row in the CSV, skipping if it's the first one, and add to list
    for row in readerObj:
        if readerObj.line_num == 1:
            continue

        csvRows.append(row)

    csvFileObj.close()

    # Write out new csv
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w')
    csvWriter = csv.writer(csvFileObj)

    for row in csvRows:
        csvWriter.writerow(row)

    csvFileObj.close()
