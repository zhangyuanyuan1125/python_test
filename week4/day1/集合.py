# -*- coding: UTF-8 -*-
__author__ = 'zhangyuanyuan_vendor@sensetime.com'
# set

# s = set() 空集合
# s = {"1", "3", "5"}
# print(type(s))
#
# # 增加一个元素
# s.add(33)
# print(s)
#
# # 增加多个元素
# s.update([66, 77])
# s.update("opso")
# print(s)
#
# # 删除
# s.remove(33)    # 删除“33”
# s.pop()         # 随机删除
# s.clear()       # 清空集合
# del s           # 删除集合


a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# 并集union
print(a.union(b))
print(a | b)

# 交集intersection
print(a.intersection(b))
print(a & b)

# 差集difference
print(a.difference(b))          # in a but not in b
print(a - b)
print(b.difference(a))          # in b but not in a
print(b - a)

# 对称差集（反向交集）symmetric_difference
print(a.symmetric_difference(b))
print(a ^ b)

# 父级(超集）
print(a.issuperset(b))      # a是否完全包含b
# 子集
print(a.issubset(b))        # a是b的子集吗

