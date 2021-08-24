#Checking for errors

import requests

#This is good practice to detect if the code halts when a bad download occurs
#Always call raise_for_status after a requests.get to make sure the site download actually worked
#Wrapping it in a try/except is also a good idea if it's not a dealbreaker

res = requests.get('https://inventwithpython.com/page_Does_not_Exist')

try:
	print(res.raise_for_status())
except Exception as e:
	print(f'There was a problem at {e}')