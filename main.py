import FetchingData as fd
import ScrapingData as sd



url = 'https://www.emobiletracker.com/'
path = 'data/scrap.html'
fd.fetchAndSaveData(url, path)

def show():
    datas = sd.table_data
    print(datas)
    
show()
