# Selective Copy

'''Write a program that walks through a folder tree and searches for files with a certain file 
extension (such as .pdf or .jpg). Copy these files from whatever location they are in to a new 
folder.
'''

from pathlib import Path
import os
import shutil

#Get a specific folder location
p = Path('/Users/ashisbitt/Desktop/AutomateTheBoringStuff/Ch.10/some_folder')
newLocation = Path('/Users/ashisbitt/Desktop/')

#Set file extention
fileExtention = '.txt'

#Get new folder name and create folder on desktop
newFolder = input('Enter new folder name: ')

if not Path.exists(newLocation / newFolder):
	os.mkdir(newLocation / newFolder)

#Walk through all subfolders using os.walk
for foldername, subfolders, filenames in os.walk(p):
	for filename in filenames:
		#Check each file for it's file extention
		if (p/filename).suffix == fileExtention:
			#copy to the new location
			shutil.copy(foldername + '/' + filename, newLocation / newFolder)
			print(f'Copying {filename}')

print("Action complete")