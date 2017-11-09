from urllib.request import urlopen
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    
    try:
        soup = BeautifulSoup(html.read())
        title = soup.body.h1
    except AttributeError as e:
        print(e)
        return None
    return title

title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title is None:
    print("Title couldn't found ")
else:
    print(title)
    

    