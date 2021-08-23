#Playing with the call stack

import traceback

def spam():
	bacon()

def bacon():
	try:
		raise Exception('Error message here')
	except:
		errorFile = open('errorInfo.txt', 'w')
		errorFile.write(traceback.format_exc())
		errorFile.close()
		print('Error written to errorInfo.txt')

spam()