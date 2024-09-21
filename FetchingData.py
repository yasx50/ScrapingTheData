import requests

def fetchAndSaveData(url, path):
    r = requests.get(url)
    
    # Saving the data into an html file in data folder
    with open(path, 'w', encoding='utf-8') as f:
        f.write(r.text)  




