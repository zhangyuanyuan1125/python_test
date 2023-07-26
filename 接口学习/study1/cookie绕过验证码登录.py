# coding:utf-8

import requests
import urllib3
urllib3.disable_warnings()
s = requests.session()

url = 'https://passport.cnblogs.com/user/signin'
r = s.get(url, verify=False)
print(r.content.decode('utf-8'))
# cookies是编辑器没有识别，不用管
c = requests.cookies.RequestsCookieJar()

c.set('.CNBlogsCookie', 'B860DF5193A9967FF445D17FCF044B0A69C69BD61E26DD4A1F2FFEC2CFAC76E8C0A7D077571'
                        '680AD50A410CA125FF0E05C0BA5B583CC4AB6296142F2C78DF98826EC7F73B37965342ECA34'
                        'F5EB713AE4AB9FF7B9')  # expiry=1564613164 可以添加多个属性

s.cookies.update(c)

# print(r.cookies)

# 访问登录之后的请求
url1 = 'https://i.cnblogs.com/EditPosts.aspx?opt=1'
r1 = s.get(url1, verify=False, cookies=c)
print(r1.content.decode('utf-8'))
