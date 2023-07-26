# coding:utf-8
# 先pip install beautifulsoup4
import pickletools

from bs4 import BeautifulSoup
yo = open('you.html', 'r')

soup = BeautifulSoup(yo, 'html.parser')  # html.parser是解析器

# # 获取title标签
# print(soup.title)
#
# # 获取title标签的文本内容
# print(soup.title.string)
#
# # 获取整个html的内容
# print(soup)

title = soup.title      # 找到title标签
print(title.name)       # 获取title的名称
print(title.string)     # 获取文本
print(title['class'])   # 获取class属性对应的值，返回的是list，只有class是list
print(title.attrs)      # 返回字典，获取所有的属性
