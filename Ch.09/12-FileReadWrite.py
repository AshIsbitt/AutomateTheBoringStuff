#File reading/writing

from pathlib import Path

#This version uses the Path library, but is particularly basic
p = Path("test.txt")
p.write_text("Hello World!")
print(p.read_text())

#By default, this opens the file in read mode
helloFile = open("test.txt")

helloContent = helloFile.read()
print(helloContent)

#Readlines instead will take each line of the file and make a list out of it
sonnetFile = open('sonnet29.txt')
print(sonnetFile.readlines())

#Writing to a file, appending to a file
#If a file does not exist when it opens in write mode, then python will create it
baconFile = open('bacon.txt', 'w')
baconFile.write("Hello Bacon\n")
baconFile.close()
baconFile = open('bacon.txt', 'a')
baconFile.write("Bacon is not a vegetable")
baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)