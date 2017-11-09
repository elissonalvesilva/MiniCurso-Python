from bs4 import BeautifulSoup
import requests

url = 'https://busca.saraiva.com.br/busca?q=barbeador'

request = requests.get(url)

objB = BeautifulSoup(request.text,'lxml')
verificaClass =  objB.find('div',class_='nm-not-found-container')

print(verificaClass)
