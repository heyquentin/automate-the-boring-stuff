from pathlib import Path
import re
workingDir = Path.cwd()

print('Welcome to the regex query program')
print('This program will tell you how many times it finds your regex query in all of your .txt files')
print('Put your .txt files into your working directory and enter the query to search for')
print('Your working directory is %s' %(workingDir))
userInput = input('Once you\'ve done that, enter your regex query here: ')

txtList = (list(workingDir.glob('*.txt')))
pattern = re.compile(r'%s' %(userInput))
regexQueryList = []

for eachFile in txtList:
    fileOpen = open(eachFile)
    fileOpen = fileOpen.read()
    matches = pattern.findall(fileOpen)
    for eachMatch in matches:
        regexQueryList.append(eachMatch)

if len(regexQueryList) == 0:
    print('Sorry, didn\'t find that query in your .txt files')
else:
    print('There are %s instances of your regex query in all .txt documents' %(len(regexQuery)))