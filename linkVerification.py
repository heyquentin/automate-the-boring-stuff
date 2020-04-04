#! Python3
import requests
import bs4

# TODO: get a response from the URL
response = requests.get('https://www.quentingauthier.com/pythonlinks/')
response.raise_for_status()

# TODO: sort out where the links actually are using Beautiful Soup
pageParse = bs4.BeautifulSoup(response.text, 'html.parser')
linkElement = pageParse.select('.entry-content a')

linkList = []
counter = 0
for i in linkElement:
    theLinks = linkElement[counter].get('href')
    linkList.append(theLinks)
    counter += 1

# TODO: test the links and report back
for eachLink in linkList:
    linkStatus = requests.get(eachLink)
    #print(linkStatus.status_code)
    if (linkStatus.status_code == requests.codes.ok):
        print('%s appears to be up and working!' %(eachLink))
    else:
        print('%s appears to be down or non-existant' %(eachLink))