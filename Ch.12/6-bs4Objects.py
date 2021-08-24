# beautiful soup

import requests
import bs4

res = requests.get("https://www.nostarch.com")
res.raise_for_status()

# This tells BS4 to read res.text using the HTML parser
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(noStarchSoup))
