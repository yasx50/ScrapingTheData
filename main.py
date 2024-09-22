from flask import Flask, jsonify, request 
import time
import FetchingData as fd
import ScrapingData as sd

app = Flask(__name__)


@app.route('/', methods=['GET'])
def show():
    url = 'https://www.emobiletracker.com/'
    path = 'data/scrap.html'
    fd.fetchAndSaveData(url, path)
    time.sleep(10)
    datas = sd.table_data
    return jsonify(datas)
    

if __name__ == '__main__':
    app.run(debug=True)