# coding:utf-8

import pymysql.cursors

connection = pymysql.connect(host='', port='', user='', password='', db='', charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    cursor = connection.cursor()  # cursor是光标
    sql = ''
    cursor.execute(sql)  # 返回的结果
    result = cursor.fetchall()  # 获取所有结果
    for data in result:
        print(result)
except Exception:
    print('查询失败！！！')

cursor.close()   # 关闭cursor
connection.close()    # 关闭连接



