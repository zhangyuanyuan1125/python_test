# coding:utf-8

import requests
from urllib import parse

url = 'http://zzk.cnblogs.com/s/blogpost?Keywords=中文'

r = requests.get(url)

print(r.url)  # 返回发url

# 对整个url解码
res = r.url
print(parse.unquote(res))

# 取出需解码的字符并解码
print(res.split('?')[1])
res1 = res.split('?')[1]
print(res1.split('=')[1])

res2 = res1.split('=')[1]
c = parse.unquote(res2)
print(c)
