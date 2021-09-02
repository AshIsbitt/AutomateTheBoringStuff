#Google maps

import webbrowser
import sys
import pyperclip

#Handle command line arguements or clipboard content
if len(sys.argv) > 1:
	address = ' '.join(sys.argv[1:])
else:
	address = pyperclip.paste()

#open browser
webbrowser.open(f'https://www.google.com/maps/place/{address}')