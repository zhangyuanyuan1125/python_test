# coding:utf-8

import unittest
from common import HTMLTestRunner

casePath = 'D:\\python_file\\接口学习\\study2\\case'

discover = unittest.defaultTestLoader.discover(casePath, 'test*.py')

# runner = unittest.TextTestRunner()
# runner.run(discover)

# 生成测试报告要下载 HTMLTestRunner.py的文件，放到python\Lib下,并且要复制到common中，再导入这个包
reportPath = 'D:\\python_file\\接口学习\\study2\\report\\'+'result.html'

fp = open(reportPath, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(fp, title='测试报告', description='报告描述')

runner.run(discover)

fp.close()
