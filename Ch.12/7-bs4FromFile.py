# bs4 from file

from bs4 import BeautifulSoup as bs4
import lxml

exampleFile = open('example.html')

# lxml is a different parser installed via pip - it's a faster parser
exampleSoup = bs4(exampleFile, 'lxml')
print(type(exampleSoup))
