import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup



url = input(" Enter - ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

#counts= dict()
#for line in html:
##    Line is in UTF-8 so we need to decode it first
#    words = line.decode().split()
#    for word in words:
#        counts[word] = counts.get(word, 0) + 1
