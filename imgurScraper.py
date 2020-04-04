#! python3
# Write a program that goes to a photo-sharing site like Flickr or Imgur, searches for a category of photos, and then opens the top 5 images in new tabs.
# You could write a program that works with any photo site that has a search feature.
import webbrowser, sys, requests, bs4

searchTerm = input('What is the search term? \n')
response = requests.get('https://imgur.com/search?q=' + searchTerm)
response.raise_for_status()
print('Status code: %s' % (response.status_code))

pageParse = bs4.BeautifulSoup(response.text, 'html.parser')
imageElem = pageParse.select('.image-list-link')

if (imageElem == []):
    print('Sorry, no hits on that search')
else:
    imageURL = 'https://imgur.com' + imageElem[0].get('href')
    for i in range(0, 5):
        imageURL = 'https://imgur.com' + imageElem[i].get('href')
        webbrowser.open(imageURL)