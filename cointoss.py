import random

ht = ['H','T']
results = []
numberOfStreaks = 0
counter = 0
headsCounter = 0
talesCounter = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    result = random.choice(ht) # chooses between H or T and stores as result
    results.append(result) # adds that result to a big list named results
    print('Toss number ' + str(counter) + ':', end=' ') # prints the toss number
    print(result) # adds the resulting H or T to the line
    counter +=1 # increments the counter

# check to see if there's any streaks
for elem in results:
    if elem == 'H':
        headsCounter +=1
        if headsCounter == 6:
            numberOfStreaks +=1
            headsCounter = 0
            talesCounter = 0
    else:
        talesCounter +=1
        if talesCounter == 6:
            numberOfStreaks +=1
            headsCounter = 0
            talesCounter = 0

# Code that checks if there is a streak of 6 heads or tails in a row.
print('Chance of streak: %s%%' % (numberOfStreaks / 100))