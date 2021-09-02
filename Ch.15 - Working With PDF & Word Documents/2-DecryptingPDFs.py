# Decrypting password protected PDFs

import PyPDF2

pdfReader = PyPDF2.PdfFileReader(open('ProvidedPDFs/encrypted.pdf', 'rb'))

print(f'Encrypted: {pdfReader.isEncrypted}')

# Enter password here
pdfReader.decrypt('rosebud')

pageObj = pdfReader.getPage(0)
