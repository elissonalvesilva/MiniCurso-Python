import urlopen from bs4
import BeautifulSoupimport
from bs4 import BeautifulSoup
import requests

url = "https://www.americanas.com.br/"
html = urlopen("http://www.pythonscraping.com/pages/page3.html")

#request  =  requests.get(url)

#soup4 = BeautifulSoup(request.text,'lxml')

#verifyId = soup4.find('div', id='sas_30352')
#verifyClass = soup4.find('div', class_="card-product-image placeholder picture")

bsObj = BeautifulSoup(html)
images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for image in images:
 print(image["src"])

print(verifyClass.split())
