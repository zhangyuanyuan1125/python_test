# 标志位讲解
exit_flag = False

for i in range(10):
    if i < 5:
        continue
    print(i)
    for j in range(10):
        print("loop:", j)
        if j == 6:
            exit_flag = True
            break
    if exit_flag:
        break
