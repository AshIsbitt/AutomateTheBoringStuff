# Encrypting PDF

import PyPDF2 as pdf

minutesFile = open('ProvidedPDFs/meetingminutes.pdf', 'rb')
pdfReader = pdf.PdfFileReader(minutesFile)

pdfWriter = pdf.PdfFileWriter()

for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))

# Encrypt the pdf with the given password
pdfWriter.encrypt('swordfish')

resultPDF = open('encryptedpdf.pdf', 'wb')
pdfWriter.write(resultPDF)
resultPDF.close()
