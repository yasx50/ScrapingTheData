import requests
from bs4 import BeautifulSoup

with open('data/scrap.html') as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc,'html.parser')


table = soup.find('table')

rows = table.find_all("tr")

#here i will store individual data in the form of list
table_data = []
for row in rows:
    cols = row.find_all(["td", "th"])  
    cols = [col.text.strip() for col in cols]  
    table_data.append(cols)
print(table_data)