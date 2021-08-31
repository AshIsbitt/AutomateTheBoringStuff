# Creating PDFs

import PyPDF2

pdfFile1Obj = open('ProvidedPDFs/meetingminutes.pdf', 'rb')
pdfFile2Obj = open('ProvidedPDFs/meetingminutes2.pdf', 'rb')

pdf1Reader = PyPDF2.PdfFileReader(pdfFile1Obj)
pdf2Reader = PyPDF2.PdfFileReader(pdfFile2Obj)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

pdfOutputFile = open('combinedMinutes.pdf', 'wb')
pdfWriter.write(pdfOutputFile)

pdfOutputFile.close()
pdfFile1Obj.close()
pdfFile2Obj.close()
