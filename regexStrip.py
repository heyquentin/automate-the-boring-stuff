'''
Write a function that takes a string and does the same thing as the strip() string method. If no other arguments are passed other than the string to strip, then whitespace characters will be
removed from the beginning and end of the string. Otherwise, the characters specified in the second argument to the function will be removed from the string.
'''

import re

# TODO: Write Function
def regexStrip(stripWhite, stripChar):
    if stripChar == '':
        startWhitePattern = re.compile(r'(^\s+)(.*)')
        startWhiteSearch = startWhitePattern.search(stripWhite)
        endWhitePattern = re.compile(r'(\s+$)')
        endWhiteSearch = endWhitePattern.search(stripWhite)

        if startWhiteSearch == None and endWhiteSearch == None:
            print('There\'s no white spaces at the beginning or end of the original sentence. Nothing to strip.')
        elif startWhiteSearch != None and endWhiteSearch == None:
            print('There\'s spaces at the beginning of the original sentence but not the end')
            remStart = startWhiteSearch.group(2)
            strippedSentence = remStart
            print('Stripped sentence: %s' %(strippedSentence))
        elif startWhiteSearch == None and endWhiteSearch != None:
            print('There\'s spaces at the end of the original sentence but not the beginning')
            endSpaces = endWhiteSearch.group(0)
            remEnd = re.sub(endSpaces, '', stripWhite)
            strippedSentence = remEnd
            print('Stripped sentence: %s' %(strippedSentence))
        elif startWhiteSearch != None and endWhiteSearch != None:
            print('There\'s spaces at both the beginning and the end of the original sentence')
            remStart = startWhiteSearch.group(2)
            endSpaces = endWhiteSearch.group(0)
            remEnd = re.sub(endSpaces, '', remStart)
            strippedSentence = remEnd
            print('Stripped sentence: %s' %(strippedSentence))

            # This was used to strip all whitespaces from beginning and end of sentence
            #remStart = startWhiteSearch.group(2)
            # endSpaces = endWhiteSearch.group(0)
            # remEnd = re.sub(endSpaces, '', remStart)
            # strippedSentence = remEnd
            # print(strippedSentence)

    else:
        characterReplace = re.sub(stripChar, '', stripWhite)
        print(characterReplace)

# TODO: Get input from user
# userInput = ''
# print('Enter your string')
# userInput = input()

# TODO: Pass input to function
#regexStrip(userInput)

# No second parameter tests
#regexStrip('This is my sentence ok','') # no spaces at beginning, no spaces at end, no second parameter, there's nothing to strip and user will be told so
#regexStrip('   This is my sentence ok','') # spaces at beginning, no spaces at end, no second parameter
#regexStrip('This is my sentence ok   ','') # no spaces at beginning, spaces at end, no second parameter
#regexStrip('   This is my sentence ok   ','') # spaces at beginning, spaces at end, no second parameter

# Second Parameter Tests
#regexStrip('   This is my sentence ok','s') # spaces at beginning, no spaces at end, second parameter. Second parameter means strip character.
#regexStrip('This is my sentence ok   ','s') # no spaces at beginning, spaces at end, second parameter. Second parameter means strip character.
#regexStrip('   This is my sentence ok   ','s') # spaces at beginning, spaces at end, second parameter. Second parameter means strip character.
#regexStrip('This is my sentence ok','s') # no spaces at beginning, no spaces at end, second parameter