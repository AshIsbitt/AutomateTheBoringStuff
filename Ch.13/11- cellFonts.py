# cell styles

from openpyxl.styles import Font
import openpyxl as xl

wb = xl.Workbook()
sheet = wb['Sheet']

# Create a font
italic24Pt = Font(size=24, italic=True)
secondFont = Font(name='Ubuntu', bold=True, size=18)

# Apply font to cell
sheet['A1'].font = italic24Pt
sheet['C2'].font = secondFont

sheet['A1'] = 'Hello World'
sheet['C2'] = 'Test'

wb.save('styles.xlsx')