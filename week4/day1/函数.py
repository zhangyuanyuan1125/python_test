# -*- coding: UTF-8 -*-
__author__ = 'zhangyuanyuan_vendor@sensetime.com'

"""
实现7！(7*6*5*4*3*2*1)，阶乘
"""

# def f(a):
#     ret = 1
#     for i in range(2, a + 1):
#         ret = ret * i
#     return ret
#
#
# print(f(7))


# 找出列表中出现一半的数字

# li = [1, 2, 3, 2, 2, 2, 5, 4, 2]
# s = set(li)
# a = len(li) / 2
# for i in s:
#     if li.count(i) > a:
#         print(i)


a = ['my', 'skills', 'are', 'poor', 'i', 'am', 'poor', 'i', 'need', 'skills', 'more', 'my', 'ability', 'are', 'so', 'poor']

print(max(a, key=lambda x: a.count(x)))

