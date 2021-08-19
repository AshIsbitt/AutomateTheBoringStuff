# Saving variables

'''
The shelve library will allow you to save variables to a binary shelf file on your local machine
This will allow for Open and Save features in your programs, or config files that can save local user settings

The shelfFile itself acts as a dictionary, and you can write to it from variables. 
Unlike normal files, shelf files don't need to be opened specifically in read or write mode
'''

import shelve

#This will create mydata.db
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('mydata')
print(type(shelfFile))
print(shelfFile['cats'])
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()
