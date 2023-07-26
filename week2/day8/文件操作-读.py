f = open('小重山', 'r', encoding='utf8')

print(f.read(5))  # 表示读取5个字符

print(f.tell())  # 打印光标所在位置，以字节为标准

f.seek(0)  # 更改光标位置
print(f.tell())
#
# print(f.readline())  # 表示读取一行
#
# print(f.readlines())   # 表示读取所有内容，以列表的形式展示

# number = 0
# for i in f.readlines():
#
#     number += 1
#     if number == 6:
#         i = ''.join([i.strip(), 'iii'])
#     print(i.strip())

# for i in f:  # fou内部将f对象做成了一个迭代器，用一个取一行
#     print(i.strip())

f.close()
