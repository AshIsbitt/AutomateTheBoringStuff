#List of filenames

from pathlib import Path

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']

for filename in myFiles:
	print(Path(r'/Users/Ash', filename))