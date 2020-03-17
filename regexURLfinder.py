import re

# TODO: Create a text variable with URLs in it
text = """But I must explain to you how all this mistaken idea of denouncing pleasure and https://www.lipsum.com/ praising pain was born and I will give you a complete account of the system, 
and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but 
because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain 
pain of itself, https://automatetheboringstuff.com/2e/chapter7/ because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. 
To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to 
enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?"""

# TODO: Create a regex to pull out the URLs
## Import the regex module with import re.
## Create a Regex object with the re.compile() function. (Remember to use a raw string.)
## Pass the string you want to search into the Regex object’s search() method. This returns a Match object.
## Call the Match object’s group() method to return a string of the actual matched text.

URLMatch = re.compile(r'http.*?\s')
matchObject = URLMatch.findall(text)

# TODO: Print the URLs from the text to the terminal
print('Here are all the URLs in your text')
for i in matchObject:
    i = i.rstrip()
    print(i)