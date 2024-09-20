import requests

http_proxy  = "http://10.10.1.10:3128"
https_proxy = "https://10.10.1.11:1080"
ftp_proxy   = "ftp://10.10.1.10:3128"

proxies = {   "http"  : http_proxy, 
              "https" : https_proxy, 
              "ftp"   : ftp_proxy
         }

def fetchAndSaveData(url,path):
    r=requests.get(url)
    with open(path,'w') as f:
        f.write(r.text)

url='https://www.emobiletracker.com/'
fetchAndSaveData(url,'data/scrap.html')
