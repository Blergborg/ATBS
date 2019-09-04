#! python3
# feelingLucky.py - opens several Google search results.

import requests, sys, webbrowser, bs4

print('Googling...')  # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text, features="lxml")  #when tried to run first time, warning said to set 'features' to lxml because no parser was specified.

# Open a browser tab for each result
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
  webbrowser.open('http://google.com' + linkElems[i].get('href'))