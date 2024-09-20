import requests
from bs4 import BeautifulSoup

with open('sample.html') as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc,'html.parser')
# print(soup.prettify)
# print(soup.title.string)
# print(soup.find_all('div')[0 ])

# for child in  soup.find(class_='container').children:
#     print(child )

# for parent in  soup.find(class_='box').parents:
#     print(parent )
#     break

cont = soup.find(class_='container');print(cont)
cont.name = 'span'
cont['class'] = 'myclass claas2'
print(cont) 