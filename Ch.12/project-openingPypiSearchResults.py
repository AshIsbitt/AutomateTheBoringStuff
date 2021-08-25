# Project - opening all google search results

import requests
import sys
import bs4
import webbrowser

print('Searching...')

res = requests.get(
    'https://www.google.com/search?q=' 'https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search results
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open a browser tab for each result
# 'package-snippet' is the name of the html class on the pypi search result box
linkElems = soup.select('.package-snippet')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = (f'https://pypi.org{linkElems[i].get('href')}')
    print(f'Opening {urlToOpen}')
    webbrowser.open(urlToOpen)
