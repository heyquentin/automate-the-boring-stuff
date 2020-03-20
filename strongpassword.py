'''
Write a function that uses regular expressions to make sure the password string it is passed is strong. A strong password is defined as one that is at least eight characters long,
contains both uppercase and lowercase characters, and has at least one digit. You may need to test the string against multiple regex patterns to validate its strength.
'''

import re
# TODO: Write the function
def passcheck(param):
    print(param)
    patternSymbol = re.compile(r'[^a-zA-Z0-9]+')
    matchSymbol = patternSymbol.search(param)
    patternNumber = re.compile(r'[0-9]+')
    matchNumber = patternNumber.search(param)
    patternLowerCase = re.compile(r'[a-z]+')
    matchPatternLowerCase = patternLowerCase.search(param)
    patternUpperCase = re.compile(r'[A-Z]+')
    matchPatternUpperCase = patternUpperCase.search(param)

    # print('debug matchSymbol: %s' %(matchSymbol))
    # print('debug matchNumber: %s' %(matchNumber))
    # print('debug matchPatternLowerCase: %s' %(matchPatternLowerCase))
    # print('debug matchPatternUpperCase: %s' %(matchPatternUpperCase))
    if (matchSymbol != None and matchNumber != None and matchPatternLowerCase != None and matchPatternUpperCase != None):
        print('You have quite the strong password there. Well done.')
    else:
        print('Your password does not meet the criteria. Please try again.')

# TODO: Get input from user
print('***** Password Validator 5000 *****')
print(''' 
Strong passwords contain:
- at least eight characters
- at least one digit
- upper and lower case
''')

userPass = ''
while not userPass:
        print('Enter your password to check if it\'s a strong one')
        userPass = input()

        if userPass != '':
            while len(userPass) < 8:
                print('Sorry, your password is too short')
                break
            else:
                passcheck(userPass)
        else:
            print('I asked you to enter your password')