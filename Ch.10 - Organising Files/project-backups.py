# Backing up a folder into a zip file

import zipfile as zf
import os

def backupToZip(folder):
	#Backup the entire contents of 'folder' to a ZIP file

	#Get the absolute path
	folder = os.path.abspath(folder)

	#Figure out the filename this folder should use
	number = 1
	while True:
		zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
		if not os.path.exists(zipFilename):
			break
		number += 1


	#Create zip file
	print(f'Creating {zipFilename}...')
	backupZip = zf.ZipFile(zipFilename, 'w')

	#Walk entire folder tree and compress each file
	for foldername, subfolders, filenames in os.walk(folder):
		print(f'adding files in {foldername}...')
		#Add current folder to zip
		backupZip.write(foldername)

		#Add all files in folder to zip
		for filename in filenames:
			newBase = os.path.basename(folder) + '_'
			#Don't back up other zip files
			if filename.startswith(newBase) and filename.endswith('.zip'):
				continue
			backupZip.write(os.path.join(foldername, filename))
	backupZip.close()

	print("Done")

backupToZip('/Users/ashisbitt/Desktop/AutomateTheBoringStuff/Ch.10/some_folder')