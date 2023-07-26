# -*- coding: UTF-8 -*-
__author__ = 'zhangyuanyuan_vendor@sensetime.com'

import json

import pytest
import yaml


class TestData:
    @pytest.mark.parametrize("a, b", [(1, 3), (4, 5)])
    # a和b是参数，可以通过字符串，列表，元组来引用，列表里的是值
    def test_01(self, a, b):
        print(a + b)

    @pytest.mark.parametrize(['c', 'd'], yaml.safe_load(open('./data.yaml')))
    # 执行yaml文件里的数据，yaml的数据为列表时：-和数据间要加空格
    def test_02(self, c, d):
        print(c + d)


class TestDemo:
    @pytest.mark.parametrize('dev', yaml.safe_load(open("./dev.yaml")))
    def test_03(self, dev):
        if "test" in dev:
            print('这是测试环境')
            print("测试环境的地址是：", dev["test"])
        elif 'icloud' in dev:
            print('这是线上环境')
            print("线上环境的地址是：", dev["icloud"])
