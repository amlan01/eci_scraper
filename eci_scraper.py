import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

#S==state code, A==constituency code, P==polling station code
url = 'http://psleci.nic.in/pslamf.aspx?S=S03&A=51&P=1'
response = requests.get(url)

#BeautifulSoup constructor
#arg1=url/html content
#arg2=name of content parser, lxml/html.parser
#url responses - 2 types(text/content)
soup = BeautifulSoup(response.text, 'html.parser')

#find_all method from bs4 allows retrieval of data by specifying html tags within 'quotes'
#also allows css class based retrieval within specified html tags
#data is retrieved in the form of list data structure

#given url response contains html table
#table data is hierarchically not organized/html tree is not the same throughout the html document
#hence multiple parsing instance
#pandas DataFrame initialization
new_table = pd.DataFrame(columns=['DS NO&NAME','AC NAME','PS NAME','Dummy#1','BUILDING QUALITY','Dummy#2','PS < 20 sqmts','Dummy#3','PS buildings dilapidated'], index = [0])

row_marker = 0
column_marker = 0
header_data1 = soup.find_all('tr')[2:4]
for tr1 in header_data1:
    for td1 in tr1.find_all('td'):
        for sp1 in td1.find_all('span'):
            for sp2 in sp1.find_all('span'):
                #print(sp2.get_text())
                new_table.iat[row_marker,column_marker] = sp2.get_text()
                column_marker += 1

header_data2 = soup.find_all('tr')[4:6]
for tr2 in header_data2:
    for td2 in tr2.find_all('td'):
        for sp3 in td2.find_all('span'):
            #print(sp1.get_text())
            new_table.iat[row_marker,column_marker] = sp3.get_text()
            column_marker += 1

list_data = soup.find_all('tr')[6:8]
for tr3 in list_data:
    #tdata = tr.find_all('td')
    #print(tdata)
    for td3 in tr3.find_all('td'):
        for sp4 in td3.find_all('span'):
            for sp5 in sp4.find_all('span'):
                #print(sp5.get_text())
                new_table.iat[row_marker,column_marker] = sp5.get_text()
                column_marker += 1
                
new_table
