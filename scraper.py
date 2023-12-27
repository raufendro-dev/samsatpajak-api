from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import json
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def jogja(query):
    # Using regular expressions
    match = re.search(r"([a-z]+)([0-9]+)([a-z]+)", query)
    if match:
        ab, digits, huruf = match.groups()
        print(f"AB: {ab}, Digits: {digits}, VE: {huruf}")
    else:
        print("No match found")
    link = "https://samsatsleman.jogjaprov.go.id/cek/pajak"
    # user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1'
    options = webdriver.ChromeOptions()
    options.add_argument("--enable-javascript")
    options.add_argument("--headless")
    # options.add_argument(f'user-agent={user_agent}')
    
    # servis = Service("chromedriver.exe")
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    driver.get(link)
    # time.sleep(1)
    textfield = driver.find_element(By.NAME, "data[CekPajak][nomor]")
    textfield2 = driver.find_element(By.NAME, "data[CekPajak][kode_belakang]")
    button_cari = driver.find_element(By.ID, "btn-cari")
    body = driver.find_element(By.TAG_NAME, "body")
    textfield.send_keys(digits)
    textfield2.send_keys(huruf)
    body.click()

    
    button_cari.click()
    time.sleep(1)
    
    driver.get_screenshot_as_file("tes.png")
    content = driver.page_source
    driver.quit()
    data = BeautifulSoup(content, 'html.parser')
    judul = []
    table = data.find("table", class_="table table-bordered")
    rows = table.find_all("tr")
    table_data = [[cell.text.strip() for cell in row.find_all("td")] for row in rows]
    judul = [row[0] for row in table_data]
    judul.remove('DATA KENDARAAN')
    print(judul)
    isi = []
    for row in table_data:
        if len(row) >= 2:
            isi.append(row[1])
    print(isi)

    json_data = {}
    for i in range(len(judul)):
        json_data[judul[i]] = isi[i]

    hasil = json.dumps(json_data, indent=4)
    print(hasil) 
    return hasil
        




    