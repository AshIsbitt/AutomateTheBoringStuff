# Writer object

import csv

outputFile = open('output.csv', 'w')
# outputWriter = csv.writer(outputFile)

# Delimiter attr changes character between the cells on a row (default is comma)
# lineterminator attr changes character at end of a row (default is newline)
outputWriter = csv.writer(outputFile, delimiter='\t', lineterminator='\n\n')

outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
outputWriter.writerow(['Hello world!', 'eggs', 'bacon', 'ham'])
outputWriter.writerow([1, 2, 3.1415926535, 4])

outputFile.close()
