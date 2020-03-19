'''
How would you write a regex that matches the full name of someone whose last name is Watanabe? You can assume that the first name that comes before it will always be one word that begins with a
capital letter. The regex must match the following:

'Haruto Watanabe'
'Alice Watanabe'
'RoboCop Watanabe'
but not the following:

'haruto Watanabe' (where the first name is not capitalized)
'Mr. Watanabe' (where the preceding word has a nonletter character)
'Watanabe' (which has no first name)
'Haruto watanabe' (where Watanabe is not capitalized)
'''

import re

text = '''
Haruto Watanabe
Alice Watanabe
RoboCop Watanabe
dumb Watanabe
Regex Watanabe
haruto Watanabe
Mr. Watanabe
Watanabe
Haruto watanabe
'''

pattern = re.compile(r'([A-Z]\w{0,10}) Watanabe')
match = pattern.findall(text)

for stupid_name in match:
    print('%s Watanabe' %(stupid_name))