# Charts

import openpyxl as xl
wb = xl.Workbook()
sheet = wb.active

# Populate table with some data
for i in range(1, 11):
	sheet[f'A{str(i)}'] = i

# Chart reference object of cells with data for chart
refObj = xl.chart.Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)

seriesObj = xl.chart.Series(refObj, title='First Series')

# Specify details about chart
chartObj = xl.chart.BarChart()
chartObj.title = 'My Chart'
chartObj.append(seriesObj)

#Create chart with top left corner in cell C5
sheet.add_chart(chartObj,'C5')

wb.save('sampleChart.xlsx')
