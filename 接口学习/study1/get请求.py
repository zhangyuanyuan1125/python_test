# coding:utf-8

import requests

url = "http://staging.senserealty.sensetime.com/senserealty/device-stat/offline-devices-count"
par = {
    'ak': 'l1-f37b7f8c-w0f55aa0948a',
    'start_timestamp': 1610347760
}
h = {

}
r = requests.get(url, params=par, headers=h)
print(r.text)
print(type(r.text))

# 最简单的转字典方法
res = r.json()
print(type(res))
