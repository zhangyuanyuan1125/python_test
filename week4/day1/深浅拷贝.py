# -*- coding: UTF-8 -*-
__author__ = 'zhangyuanyuan_vendor@sensetime.com'

# 浅拷贝:只拷贝第一层

a = [[1, 2], 3, 4]
b = a.copy()

# b[1] = 333
# print(a, b)         # a = [[1, 2], 3, 4]      b = [[1, 2], 333, 4]

b[0][0] = 111
print(a, b)             # a = [[111, 2], 3, 4]      b = [[111, 2], 3, 4]


# 深拷贝：复制全部

# import copy
#
# m = [[0, 11], 22, 33]
# n = copy.deepcopy(m)
#
# # n[1] = 2
# # print(m, n)          # m = [[0, 11], 22, 33]      n = [[0, 11], 2, 33]
#
# n[0][0] = 66666
# print(m, n)             # m = [[0, 11], 22, 33]     n = [[66666, 11], 22, 33]


