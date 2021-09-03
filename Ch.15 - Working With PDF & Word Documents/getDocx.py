# Getting Full text fromm a docx file
# This should be file 8 but import doesn't like the numbers in the filename (see file 9)

import docx

# This gets the raw text, not the styling
def getText(filename):
	doc = docx.Document(filename)
	fullText = []

	for paragraph in doc.paragraphs:
		fullText.append(paragraph.text)

	return '\n'.join(fullText)