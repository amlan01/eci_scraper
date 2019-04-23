# -*- coding: cp1252 -*-
import requests
from bs4 import BeautifulSoup

#BeautifulSoup is a module, that generates BeautifulSoup object that is, a parse tree from the parsed page(url) that we get from running Python built-in html.parser over the HTML.

url = 'http://psleci.nic.in/pslamf.aspx?S=S03&A=51&P=1'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())

#print(soup.prettify()) will print content of page in a beautifully parsed hierarhical manner. Find specific tags and classe/id within tags such as p,tr,td and all. list_data = soup.find_all('span', id='Label1')

list_data = soup.find_all('tr')
list_data
