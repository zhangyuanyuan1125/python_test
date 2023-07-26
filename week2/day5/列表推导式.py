# -*- coding: UTF-8 -*-
__author__ = 'zhangyuanyuan_vendor@sensetime.com'

# 生成一个平方列表
li1 = []
for i in range(1, 4):
    li1.append(i*i)
print(li1)

# 列表推导式
li2 = [i**2 for i in range(1, 4)]
print(li2)

# 有判断条件时使用列表推导式
li3 = [i**2 for i in range(1, 4) if i != 1]
print(li3)

# 嵌套的列表推导式
li4 = [i*j for i in range(1, 4) for j in range(1, 4)]
print(li4)
