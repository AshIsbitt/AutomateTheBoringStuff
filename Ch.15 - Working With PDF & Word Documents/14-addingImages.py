# Adding images

import docx

doc = docx.Document()

# Width and height are optional parameters and can use either inches or cm when specifying
doc.add_picture('zophie.PNG', width=docx.shared.Inches(1), height=docx.shared.Cm(4))

doc.save('14-zophie.docx')