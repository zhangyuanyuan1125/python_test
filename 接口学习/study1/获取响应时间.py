# coding:utf-8

import requests

r = requests.get('https://www.baidu.com/s')
print(r.elapsed.total_seconds())