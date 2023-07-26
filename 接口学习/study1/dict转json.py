# coding:utf-8

import json

d = {
    'a': 111,
    'b': '255',
    'c': True
}

# 字典转json
d_json = json.dumps(d)
print(d_json)

# json转字典
# j_dict = json.loads(d_json)
# j_dict = j_dict.json()
