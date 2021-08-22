#Creating and adding to ZIP files

import zipfile as zf

#This will create a new zip file called newZip.zip
#You can also add to existing zip files with 'a' Append mode
newZip = zf.ZipFile('newZip.zip', 'w')

#This adds the existing file newfile.txt to the ZIP file using the specified compression type
#Just use ZIP_DEFLATED as a standard
newZip.write('newfile.txt', compress_type=zf.ZIP_DEFLATED)

newZip.close()