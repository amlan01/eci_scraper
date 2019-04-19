import requests
from bs4 import BeautifulSoup

webaddr = 'http://psleci.nic.in/pslamf.aspx?S=S03&A=25&P=1'
response = requests.get(webaddr)
soup = BeautifulSoup(response.text, 'html.parser')

print(soup)
