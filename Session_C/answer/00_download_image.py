import requests
from bs4 import BeautifulSoup
from urllib.request import build_opener
from urllib.request import install_opener
from urllib.request import urlretrieve

# 取得目標網頁
response = requests.get('https://gushi.tw/hu-shih-memorial-hall/')

# 透過 Beautifulsoup 解析網頁
soup = BeautifulSoup(response.text, 'lxml')

# 取得所有的圖片 tag
image = soup.find_all('img')

# 檢查第一個 img tag
print(u'圖片 tag:')
print(image[0].prettify())

# 取得第一個圖片位置資訊
print(u'圖片位置資訊:')
print(image[0]['src'])

# 增加 opener 偽裝成瀏覽器發送請求
opener = build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36')]
install_opener(opener)

# 顯示進度的 callback
def check_percentage(chunk, chunk_size, remote_size):
    percentage = 100.0 * chunk * chunk_size / remote_size
    if percentage > 100.0:
        percentage = 100.0
    print('Download...{:.2f}%'.format(percentage))

# 下載圖片
urlretrieve(image[0]['src'], 'logo.png', check_percentage)