# Overlaying pages

'''
This allows you to overlay one page on top of another.
This is useful for adding watermarks or logos to PDFs
'''

import PyPDF2 as pdf

minutesFile = open('ProvidedPDFs/meetingminutes.pdf', 'rb')
pdfReader = pdf.PdfFileReader(minutesFile)
minutesFirstPage = pdfReader.getPage(0)

watermarkReader = pdf.PdfFileReader(open('ProvidedPDFs/watermark.pdf', 'rb'))

minutesFirstPage.mergePage(watermarkReader.getPage(0))

pdfWriter = pdf.PdfFileWriter()
pdfWriter.addPage(minutesFirstPage)

for pageNum in range(1, pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

resultPDFFile = open('5-watermarkedCover.pdf', 'wb')
pdfWriter.write(resultPDFFile)

minutesFile.close()
resultPDFFile.close()
