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

name_ja = soup.select('.bg_box h1')
name_en = soup.select('.bg_box h1 span')
catch = soup.select('.catch')
mp4 = soup.select('.txt video')
mp4_gif = soup.select('.txt img')
snsList = soup.select('.t_sns li a')
recommendList = soup.select('.talent_youtube li a')

print(''.join(name_ja[0].find_all(text=True, recursive=False)))
print(name_en[0].get_text())
print(catch[0].get_text())
if mp4:
    print(mp4[0].get('src'))
elif mp4_gif:
    print(mp4_gif[0].get('src'))

for sns in snsList:
    if 'https://twitter.com' in sns.get('href'):
        print(sns.get('href'))
    if 'youtube' in sns.get('href'):
        print(sns.get('href'))

for recommend in recommendList:
    print(recommend.get('href'))

# out_folder = Path('downloaded')
# out_folder.mkdir(exist_ok=True)

# imgs = soup.select('img')
# for img in imgs:
#     src = img.get('src')
#     img_url = urllib.parse.urljoin(load_url, src)
#     loaded_img = requests.get(img_url)
#     file_name = img.get('src').split('/')[-1]
#     out_path = out_folder.joinpath(file_name)
#     with open(out_path, 'wb') as file:
#         file.write(loaded_img.content)
#     time.sleep(1)