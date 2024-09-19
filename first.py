import requests

def fetchAndSaveData(url,path):
    r=requests.get(url)
    with open(path,'w') as f:
        f.write(r.text)

url='https://www.emobiletracker.com/'
fetchAndSaveData(url,'data/scrap.html')
