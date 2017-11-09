from urllib.request import urlopen
from bs4 import BeautifulSoup



try:
html = urlopen("http://www.pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
else:
    
if html is None:
    print("URL not found")
else:
    


