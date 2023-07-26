# -*- coding: UTF-8 -*-
__author__ = 'zhangyuanyuan_vendor@sensetime.com'

li = [5, 3, 9, 0, 1, 8]

for i in range(len(li) - 1):
    for j in range(len(li) - 1 - i):
        if li[j] > li[j + 1]:
            li[j], li[j + 1] = li[j + 1], li[j]
print(li)
