# Pretty printing

import pprint as pp

cats = [{'name':'Zophie', 'desc':'chubby'}, {'name':'Pooka', 'desc':'fluffy'}]
pp.pformat(cats)

fileObj = open('myCats.py', 'w')
fileObj.write('cats =' + pp.pformat(cats) + '\n')
fileObj.close()