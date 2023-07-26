# -*- coding: UTF-8 -*-
__author__ = 'zhangyuanyuan_vendor@sensetime.com'

import xlwt

workbook = xlwt.Workbook(encoding='utf-8')

table = workbook.add_sheet('设施清单20211028145447.xlsx')

for i in range(0, 30001):
    table.write(i, 0, '武馆_修改后')
    table.write(i, 1, '设备房000%s' % (i,))
    table.write(i, 2, '设备房')
    table.write(i, 3, '设备房000%s' % (i,))

workbook.save('设施清单20211028145447.xlsx')
