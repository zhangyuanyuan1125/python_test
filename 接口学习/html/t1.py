# coding:utf-8

import requests
from bs4 import BeautifulSoup

r = requests.get('http://699pic.com/sousuo-218808-13-1-0-0-0.html')

m = r.content.decode('utf-8')

soup = BeautifulSoup(m, 'html.parser')

texts = soup.find_all('span')  # 返回的是list

for i in texts:
    print(i.get_text().replace('\n', ''))


