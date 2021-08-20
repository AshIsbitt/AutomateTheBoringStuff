#Multi-clipboard

'''
Usage:
Python3 mcb.pyw save <keyword> - Saves clipboard to keyword
Python3 mcb.pyw <keyword> - loads keyword to clipboard
Python3 mcb.pyw list  - loads all keywords to clipboard
'''

import shelve
import sys
import pyperclip
import pyinputplus as pyin
import os

mcbShelve = shelve.open('mcb')

#Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbShelve[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 2:
	#list keywords and load content
	if sys.argv[1].lower() == 'list':
		print(str(list(mcbShelve.keys())))
		#pyperclip.copy(str(list(mcbShelve.keys())))
	elif sys.argv[1] in mcbShelve:
		pyperclip.copy(mcbShelve[sys.argv[1]])

#extending the program with <del> and <delall> functionality
if len(sys.argv) == 3 and sys.argv[1].lower() == 'del':
	mcbShelve.pop(str(sys.argv[2]))
elif len(sys.argv) == 2 and sys.argv[1].lower() == 'delall':
	validationAsk = pyin.inputYesNo("Are you sure? ")
	if validationAsk == 'yes':
		mcbShelve.close()
		os.remove('mcb.db')


mcbShelve.close()
