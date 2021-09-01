# Project - combining selecct pages from multiples PDFs

'''
Say you have the boring job of merging several dozen PDF documents into a single PDF file. 
Each of them has a cover sheet as the first page, but you don’t want the cover sheet repeated 
in the final result. Even though there are lots of free programs for combining PDFs, many of 
them simply merge entire files together.
'''

import PyPDF2 as pdf
import os

# Get all the PDF filenames
pdfFiles = []

for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

pdfFiles.sort(key=str.lower)
pdfWriter = pdf.PdfFileWriter()

# Loop through all PDF files
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = pdf.PdfFileReader(pdfFileObj)

    # Loop through each page and add them
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# Save resulting PDF to file
pdfOutput = open('p-allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
