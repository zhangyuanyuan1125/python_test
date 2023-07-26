# coding:utf-8

import requests
from bs4 import BeautifulSoup
import os
r = requests.get('http://699pic.com/sousuo-218808-13-1-0-0-0.html')

m = r.content.decode('utf-8')

soup = BeautifulSoup(m, 'html.parser')
alls = soup.find_all(class_='lazy')

for i in alls:
    try:
        # print(i['data-original'])
        url = 'http:'+i['data-original']
        name = i['title']
        r1 = requests.get(url)
        path = 'D:\\python_file\\接口学习\\html\\images'
        if not os.path.exists(path):
            os.mkdir(path)
        else:
            fp = open(path+'\\%s.jpg' % name, 'wb')  # 保存到其他文件夹open('D:\\test\\%s.jpg % name, 'wb)
            fp.write(r1.content)
            fp.close()
    except Exception as msg:
        print(msg)



