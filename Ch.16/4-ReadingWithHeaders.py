# Dictreader

# These are used when there's a header bar at the top of the CSV and uses dictionaries with the headers as keys

import csv

exampleFile = open('exampleWithHeader.csv')
exampleDictReader = csv.DictReader(exampleFile)

for row in exampleDictReader:
    print(row['Timestamp'], row['Fruit'], row['Quantity'])
