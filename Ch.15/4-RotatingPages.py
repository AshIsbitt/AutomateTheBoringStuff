# Rotating PDF pages

import PyPDF2 as pdf

pdfFileObj = open('ProvidedPDFs/meetingminutes.pdf', 'rb')
pdfReader = pdf.PdfFileReader(pdfFileObj)

page = pdfReader.getPage(0)
page.rotateClockwise(90)

pdfWriter = pdf.PdfFileWriter()
pdfWriter.addPage(page)

resultPDFFile = open('4-rotatedPage.pdf', 'wb')
pdfWriter.write(resultPDFFile)
resultPDFFile.close()
pdfFileObj.close()
