'''
How would you write a regex that matches a sentence where the first word is either Alice, Bob, or Carol; the second word is either eats, pets, or throws; the third word is apples, cats,
or baseballs; and the sentence ends with a period? This regex should be case-insensitive.
'''

import re

text = '''
# match the following
Alice eats apples.
Bob pets cats.
Carol throws baseballs.
Alice throws Apples.
BOB EATS CATS.
# but not
RoboCop eats apples.
ALICE THROWS FOOTBALLS.
Carol eats 7 cats.
'''

# TODO: match a sentence where the first word is either Alice, Bob, or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs
pattern = re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples.|cats.|baseballs.)', re.I)
match = pattern.finditer(text)
matchConcat = pattern.finditer(text)

for i in match:
    print(i[0])

# or you can concatenate the groups
print(' ')
for j in matchConcat:
    print('%s %s %s' %(j[1],j[2],j[3]))