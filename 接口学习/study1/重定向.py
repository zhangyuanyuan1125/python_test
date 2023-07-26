# coding:utf-8

import requests
import urllib3
urllib3.disable_warnings()
host = 'https://i.cnblogs.com/'

s = requests.session()
url = 'https://i.cnblogs.com/EditPosts.aspx?opt=1'

r1 = s.get(url, verify=False)
# print(r1.url)
# print(r1.status_code)

# # 禁止重定向，找到中间的地址
# r2 = s.get(url, verify=False, allow_redirects=False) # allow_redirects=False禁止重定向
# print(r2.status_code)
# print(r2.url)
# print(r2.headers['location'])
# # 重定向后的地址
# print(host + r2.headers['location'])  # urlencode编码

# history重定向历史记录
print(r1.history)
for i in r1.history:
    print(i.status_code)
    print(i.url)
    print(i.headers)


