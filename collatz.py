import sys

def collatz(number):
    global userInput
    if (userInput % 2 == 0):
        userInput = int(userInput / 2)
        print('number // 2: ' + str(userInput))
    else:
        userInput = int(userInput * 3 + 1)
        print('3 * the number above + 1 is ' + str(userInput))

loopCondition = 0

while not loopCondition:
    try:
        userInput = int(input('Enter a number: '))
        loopCondition=1
    except ValueError:
        print('That\'s not a number.')
    except:
        print('Something went wrong. Please try again.')

if userInput <=0:
    print('That number isn\'t going to work for the Collatz Sequence')
else:
    while userInput >1:
        collatz(userInput)
        if userInput == 1:
            print('That\'s the Collatz Sequence!')