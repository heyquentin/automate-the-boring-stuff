import random
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

guess = ''
while guess not in ('heads', 'tails', 'hacker'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    logging.debug('guess is: %s' % (guess))

toss = random.randint(0, 1) # 0 is tails, 1 is heads
logging.debug('0 is tails, 1 is heads. toss is: %s' %(toss))

if guess == 'hacker':
    print('You\'ve accessed the secret menu where I will set the \'toss\' value to be something that it never should be')
    print('That means you get to see the \'assert\' error statement. Lucky you!')
    toss = 3
    assert (toss == 0 or toss == 1), 'In toss, 0 is tails and 1 is heads. I forced toss to be 3. This should never happen. That\'s why you\'re reading this error'

if toss == 0:
    toss = 'tails'
else:
    toss = 'heads'

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')