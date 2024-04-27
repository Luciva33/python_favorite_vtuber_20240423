import urllib.parse
import requests
from bs4 import BeautifulSoup
from pathlib import Path # フォルダ操作モジュール
import urllib   # url操作モジュール
import time # 時間操作モジュール

load_url = 'https://hololive.hololivepro.com/talents/harusaki-nodoka/'
res = requests.get(load_url)
res.encoding = res.apparent_encoding
soup = BeautifulSoup(res.text, 'html.parser')

data_dts = soup.select('.talent_data dl dt')
data_dds = soup.select('.talent_data dl dd')

print('---------- dt ------------')
for dt in data_dts:
    print(dt.get_text())

print('---------- dd ------------')
for dd in data_dds:
    print(str(dd))