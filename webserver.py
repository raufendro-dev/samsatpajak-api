import scraper
from flask import Flask, render_template, request, redirect, session
import logging
app = Flask(__name__)
logging.basicConfig(filename="logpengunjung.log", level=logging.INFO)
@app.route('/samsat/jogja',  methods=['GET'])
def jalanweb():
    if request.method == 'GET':
        cari = request.args['nopol']

        hasil = scraper.jogja(cari)
        ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr) 
        asal = request.headers.get('User-Agent')
        ambillog = 'IP Address: '+ip+'\n'+'User Agent: '+asal+'\n'+'Query Search: '+cari
        logging.info(ambillog)

    return hasil
 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=86)
