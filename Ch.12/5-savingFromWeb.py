#Saving downloaded files to HDD

import requests

res = requests.get('https://AutomateTheBoringStuff.com/files/rj.txt')
res.raise_for_status()

#To save the unicode encoding, make sure to open the file as wb mode - write binary mode
playFile = open('romeo+juliet.txt', 'wb')

#iter_content specifies how many bytes of data per chunk there are, 100000 is generally a good number
for chunk in res.iter_content(100000):
	playFile.write(chunk)

playFile.close()