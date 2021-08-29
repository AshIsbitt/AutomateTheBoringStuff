# Column and Row addressing

import ezsheets as ez

print(ez.convertAddress('A2'))
print(ez.convertAddress(1, 2))

print(ez.getColumnNumberOf('B'))
print(ez.getColumnLetterOf(999))
