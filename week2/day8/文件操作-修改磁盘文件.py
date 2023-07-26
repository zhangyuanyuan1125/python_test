# f = open('小重山', 'r', encoding='utf8')
#
# a = open('小重山备份', 'w', encoding='utf8')
#
# number = 0
# for line in f:
#
#     number += 1
#     if number == 4:
#         line = ''.join([line.strip(), 'hello\n'])
#     a.write(line)
#
# f.close()
# a.close()

with open('小重山', 'r', encoding='utf8') as f_read, open('小重山备份', 'w', encoding='utf8') as f_write:
    pass
