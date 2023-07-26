# coding:utf-8

import requests

# # 正则提取
# import re
#
# # 知道前后取中间，例：postid=5846254&
# a = 'blagnljmpostid=5846254&'
# postid = re.findall("postid=(.+?)&", a)[0]
# print(postid)


# import hmac
# import hashlib
#
# appkey = "one"
# strToSign = "six"
# # # hmac_sha256加密
# # signature = hmac.new(bytes(appkey, encoding='utf-8'), bytes(strToSign, encoding='utf-8'),
# #                      digestmod=hashlib.sha256).digest()
# # print(signature)
# # 二进制转为HEX
# # HEX = signature.hex()
# # print(HEX)
# # # # 将字符串换为小写
# # lowsigne = HEX.lower()
# # print(lowsigne)
# #
# s = hmac.new(bytes(appkey, encoding='utf-8'), bytes(strToSign, encoding='utf-8'),
#              digestmod=hashlib.sha256).hexdigest().lower()
# print(s)


# 参数化
s = requests.session()
url = 'https://www.baidu.com'
body = {
    'user': 'zhang',
    'pwd': 'xxegwgg'
}
r = s.post(url, json=body)
res_token = r.json()

url1 = 'https://www.baidu.com?he=%s' % res_token   # 参数化，或者直接定义一个头部
h = {
    'token': res_token
}
