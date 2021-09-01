# Dictwriter

import csv

outputFile = open('output.csv', 'w')
outputDictWriter = csv.DictWriter(outputFile, ['Name', 'Pet', 'Phone'])

# Create the header with the given list above
outputDictWriter.writeheader()

outputDictWriter.writerow({'Name': 'Alice', 'Pet': 'Cat', 'Phone': '555-1234'})
outputDictWriter.writerow({'Name': 'Bob', 'Phone': '555-9999'})
outputDictWriter.writerow({'Pet': 'dog', 'Phone': '555-5555', 'Name': 'Carol'})

outputFile.close()
