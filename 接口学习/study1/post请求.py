# coding:utf-8

import requests

s = requests.session()  # 定义浏览器

url = 'http://staging.senserealty.sensetime.com/senserealty/api/sensego/console/v1.0/login'

body = {
    "pwd": "c784d3e38821a2e883da426a24f22809",
    "user_name": "zyy_0902"
}
r = s.post(url, json=body)
r_dict = r.json()
print(r_dict['token'])
