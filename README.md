# Samsat Pajak API

Samsat Pajak API adalah API unofficial untuk mendapatkan data cek pajak kendaraan bermotor berbentuk json. Samsat Pajak API merupakan web scraping dari beberapa halaman samsat di Indonesia

Link Samsat DI Yogyakarta : https://samsatsleman.jogjaprov.go.id/cek/pajak


### Run
#### DI Yogyakarta
Live link sample : http://103.193.178.139:8686/samsat/jogja?nopol=ab4444zq

Parameter nopol adalah parameter nomor polisi kendaraan


## Cara penggunaan

### Install Library Python
Pertama install terlebih dahulu library python berikut
- Flask
- BeautifulSoup4
- Selenium
### Run WebServer
Jalankan file webserver
- python3 webserver.py
- buka pada browser, contoh : http://localhost:8686/samsat/jogja?nopol=ab4444zq

### Catatan
- Link pada browser bisa menggunakan ip atau domain anda
- Port bisa diubah di webserver.py
- File logpengunjung.log adalah log dari pencarian user. Anda bisa menggunakannya jika dibutuhkan