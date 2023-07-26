# -*- coding: UTF-8 -*-
__author__ = 'zhangyuanyuan_vendor@sensetime.com'

import time


class Person:  # 创建类用class，且需使用大驼峰命名
    name1 = 'zhangyuanyuan'  # 属性

    def __init__(self):  # init方法用来添加属性
        self.name = 'zhang'

    def eat(self):  # 方法用def创建
        # print("%s正在吃" % self.name)
        return f'{self.name}正在吃'  # 格式化输出的两种方法


a = Person()  # 调用类需将类示例化
print(a.name1)
print(a.eat())
